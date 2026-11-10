#!/usr/bin/env python3
"""Verifica contratos de domínio v0.1 inteiramente offline.

Este checker usa ``jsonschema.Draft202012Validator`` com ``FormatChecker`` e
faz somente validação estrutural, relações entre fixtures sintéticas,
canonicalização/hash do conteúdo, timestamps e invariantes de autoridade
fechada. Não é policy de permissão em runtime, não autentica autores, não
prova tenant isolation real, não executa endpoints/aplicação, não implementa
cadastro normativo médico e não transforma hash em assinatura legal ou
integridade externa. A data ``FIXTURE_NOW`` serve somente para tornar a
verificação determinística; não representa relógio de produção.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:  # pragma: no cover - mensagem de ambiente
    raise SystemExit("jsonschema é obrigatório para os contratos de domínio") from exc

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from build_domain_contracts import (  # noqa: E402
    CANONICALIZATION_VERSION,
    SCHEMA_NAMES,
    canonical_content_bytes,
    content_sha256,
)

FIXTURE_NOW = datetime.fromisoformat("2026-11-10T12:00:00-03:00")
FIXTURE_DATE = date(2026, 11, 10)
LIMITATIONS = [
    "Somente contratos JSON, relações sintéticas e invariantes locais; não é policy de permissão runtime.",
    "Não autentica author_id, registro profissional ou identidade humana e não prova isolamento real de clinic/tenant.",
    "Hash prova apenas bytes canônicos de content-json-v1; não é assinatura, autoria, validade clínica ou integridade externa.",
    "FIXTURE_NOW é uma data explícita de fixture, não o relógio atual nem uma regra operacional de produção.",
    "Não executa endpoints, aplicação, armazenamento, antivírus, exportação, cadastro normativo médico ou fluxos legais.",
]


def load_json(path: Path) -> Any:
    """Lê JSON UTF-8 sem rede; rejeita constantes numéricas não JSON."""
    def invalid_constant(value: str) -> None:
        raise ValueError(f"constante JSON inválida: {value}")

    return json.loads(path.read_text(encoding="utf-8"), parse_constant=invalid_constant)


def load_contracts(root: Path = ROOT) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    """Carrega os sete schemas e exemplos correspondentes, sem gerar/modificar arquivos."""
    schemas: dict[str, dict[str, Any]] = {}
    examples: dict[str, dict[str, Any]] = {}
    for name in SCHEMA_NAMES:
        schema_path = root / "schemas" / f"{name}.schema.json"
        example_path = root / "examples" / f"{name}.example.json"
        schemas[name] = load_json(schema_path)
        examples[name] = load_json(example_path)
    return schemas, examples


def schema_errors(name: str, instance: Any, schema: dict[str, Any]) -> list[str]:
    """Retorna erros Draft 2020-12 formatados para uma instância."""
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{name}: {error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
    ]


def parse_aware(value: str, field: str) -> datetime:
    """Converte ISO datetime e exige offset; não valida relógio de produção."""
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field}: datetime inválido") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError(f"{field}: datetime precisa ser timezone-aware")
    return parsed


def require(condition: bool, message: str, errors: list[str]) -> None:
    """Acumula uma falha local, sem interpretar autorização de runtime."""
    if not condition:
        errors.append(message)


def validate_positive_examples(
    schemas: dict[str, dict[str, Any]], examples: dict[str, dict[str, Any]]
) -> list[str]:
    """Valida todos os pares schema/example com Draft 2020-12 e formatos."""
    errors: list[str] = []
    for name in SCHEMA_NAMES:
        errors.extend(schema_errors(name, examples[name], schemas[name]))
    return errors


def validate_invariants(examples: dict[str, dict[str, Any]]) -> list[str]:
    """Verifica somente invariantes sintéticas de hash, autoridade, tenant e IDs."""
    errors: list[str] = []
    patient = examples["patient"]
    draft = examples["draft-command"]
    finalize = examples["finalize-command"]
    snapshot = examples["record-snapshot"]
    addendum = examples["addendum-command"]
    attachment = examples["attachment"]
    export_job = examples["export-job"]

    try:
        birth_date = date.fromisoformat(patient["birth_date"])
        require(birth_date <= FIXTURE_DATE, "patient.birth_date não pode estar no futuro da fixture", errors)
    except (KeyError, TypeError, ValueError):
        errors.append("patient.birth_date não é uma data ISO válida")

    # O snapshot deve carregar uma autoria declarada pelo servidor, enquanto os
    # comandos client-side fechados não aceitam author/status/tenant derivados.
    require(bool(snapshot.get("author_id")), "record-snapshot.author_id ausente", errors)
    require(bool(snapshot.get("professional_registration")), "record-snapshot.professional_registration ausente", errors)
    for command_name, command in (("draft-command", draft), ("finalize-command", finalize), ("addendum-command", addendum)):
        forbidden = {"author", "author_id", "clinic_id", "patient_id", "status"} & set(command)
        require(not forbidden, f"{command_name}: campos derivados/autoridade no input fechado: {sorted(forbidden)}", errors)
    require("status" not in draft and "status" not in finalize, "comando client-side não pode enviar status", errors)
    require("content" not in finalize, "finalize-command não pode enviar content", errors)

    # Hash canônico é conteúdo apenas; json.dumps é deliberadamente explícito.
    try:
        expected_hash = content_sha256(snapshot["content"])
        require(snapshot["canonicalization_version"] == CANONICALIZATION_VERSION, "canonicalization_version inesperada", errors)
        require(snapshot["content_sha256"] == expected_hash, "record-snapshot.content_sha256 não corresponde ao content canônico", errors)
        require(
            canonical_content_bytes(snapshot["content"]) == __import__("json").dumps(
                snapshot["content"], ensure_ascii=False, sort_keys=True, separators=(",", ":")
            ).encode("utf-8"),
            "canonicalização content-json-v1 divergente",
            errors,
        )
    except (KeyError, TypeError, ValueError):
        errors.append("record-snapshot.content não permite calcular hash canônico")

    content = snapshot.get("content", {})
    clinical_fields = ("chief_complaint", "history", "observations", "assessment", "plan")
    require(
        any(isinstance(content.get(field), str) and content[field].strip() for field in clinical_fields),
        "record-snapshot.content precisa de ao menos uma string clínica não vazia",
        errors,
    )
    allergy_status = content.get("allergy_status")
    allergy_details = content.get("allergy_details")
    if allergy_status == "known":
        require(isinstance(allergy_details, str) and bool(allergy_details.strip()), "allergy_status=known exige allergy_details", errors)
    elif allergy_status in ("not_recorded", "none_reported"):
        require(allergy_details is None, f"allergy_status={allergy_status} exige allergy_details=null", errors)

    # Relações da fixture não são autorização: são somente consistência de IDs.
    require(snapshot.get("clinic_id") == patient.get("clinic_id"), "snapshot/patient clinic_id divergente", errors)
    require(snapshot.get("patient_id") == patient.get("id"), "snapshot/patient_id divergente", errors)
    identity = snapshot.get("patient_identity", {})
    for key in ("full_name", "birth_date", "local_number"):
        require(identity.get(key) == patient.get(key), f"snapshot.patient_identity.{key} divergente da fixture", errors)
    require(snapshot.get("encounter_id") == draft.get("encounter_id"), "snapshot/draft encounter_id divergente", errors)
    require(attachment.get("clinic_id") == patient.get("clinic_id"), "attachment/patient clinic_id divergente", errors)
    require(attachment.get("patient_id") == patient.get("id"), "attachment/patient_id divergente", errors)
    require(attachment.get("encounter_id") == snapshot.get("encounter_id"), "attachment/encounter_id divergente", errors)
    require(addendum.get("snapshot_id") == snapshot.get("id"), "addendum/snapshot_id divergente", errors)
    require(export_job.get("clinic_id") == patient.get("clinic_id"), "export-job/patient clinic_id divergente", errors)
    require(export_job.get("patient_id") == patient.get("id"), "export-job/patient_id divergente", errors)
    require(snapshot.get("id") in export_job.get("snapshot_ids", []), "export-job não referencia snapshot da fixture", errors)
    require(attachment.get("id") in export_job.get("attachment_ids", []), "export-job não referencia attachment da fixture", errors)

    # Timestamps: aware, finalização não anterior ao encounter e data futura
    # proibida somente em relação à data explícita da fixture; encounter
    # backdated é permitido e não há inferência sobre admission timestamp.
    try:
        encounter_at = parse_aware(snapshot["encounter_at"], "record-snapshot.encounter_at")
        finalized_at = parse_aware(snapshot["finalized_at"], "record-snapshot.finalized_at")
        require(finalized_at >= encounter_at, "record-snapshot.finalized_at não pode ser anterior a encounter_at", errors)
        require(encounter_at <= FIXTURE_NOW, "record-snapshot.encounter_at não pode estar no futuro da fixture", errors)
        require(finalized_at <= FIXTURE_NOW, "record-snapshot.finalized_at não pode estar no futuro da fixture", errors)
    except (KeyError, TypeError, ValueError) as exc:
        errors.append(str(exc))
    try:
        if attachment.get("scanned_at") is not None:
            parse_aware(attachment["scanned_at"], "attachment.scanned_at")
        if export_job.get("expires_at") is not None:
            expiry = parse_aware(export_job["expires_at"], "export-job.expires_at")
            if export_job.get("status") == "ready":
                require(expiry > FIXTURE_NOW, "export-job ready precisa expirar depois de FIXTURE_NOW", errors)
    except (KeyError, TypeError, ValueError) as exc:
        errors.append(str(exc))

    if attachment.get("status") == "clean":
        require(bool(attachment.get("scan_engine_version")), "attachment clean exige scan_engine_version", errors)
        require(bool(attachment.get("scanned_at")), "attachment clean exige scanned_at", errors)
    require(snapshot.get("status") == "finalized", "record-snapshot precisa ser finalized, não draft", errors)
    require(finalize.get("expected_version", 0) >= 1, "finalize-command.expected_version precisa ser >= 1", errors)
    return errors


def run_checks(root: Path = ROOT) -> dict[str, Any]:
    """Executa a checagem offline e retorna relatório serializável."""
    errors: list[str] = []
    try:
        schemas, examples = load_contracts(root)
        for schema in schemas.values():
            Draft202012Validator.check_schema(schema)
        errors.extend(validate_positive_examples(schemas, examples))
        errors.extend(validate_invariants(examples))
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        errors.append(f"falha ao carregar contratos: {exc}")
    return {
        "status": "fail" if errors else "pass",
        "schema_count": len(SCHEMA_NAMES),
        "example_count": len(SCHEMA_NAMES),
        "errors": errors,
        "limitations": LIMITATIONS,
        "fixture_now": FIXTURE_NOW.isoformat(),
        "scope": "offline_domain_contracts_only",
    }


def main(argv: Iterable[str] | None = None) -> int:
    """CLI determinística: lê arquivos, não os modifica."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=str(ROOT), help="raiz do projeto")
    args = parser.parse_args(list(argv) if argv is not None else None)
    result = run_checks(Path(args.project).expanduser().resolve())
    print(result["status"].upper(), "— offline_domain_contracts")
    print(f"Schemas verificados: {result['schema_count']}")
    print(f"Examples verificados: {result['example_count']}")
    for error in result["errors"]:
        print("ERRO:", error)
    print("LIMITES:", " ".join(result["limitations"]))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
