#!/usr/bin/env python3
"""Gera contratos de domínio v0.1 e fixtures sintéticas, sem rede ou LLM.

O conteúdo gerado é declarativo e offline. Estes contratos não implementam
cadastro médico normativo, autorização de runtime, assinatura eletrônica,
integridade externa, endpoints ou regras legais. O hash do snapshot só prova
os bytes canônicos do campo ``content``.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = ROOT / "schemas"
EXAMPLES_DIR = ROOT / "examples"
SCHEMA_VERSION = "0.1"
CANONICALIZATION_VERSION = "content-json-v1"

SCHEMA_NAMES = (
    "patient",
    "draft-command",
    "finalize-command",
    "record-snapshot",
    "addendum-command",
    "attachment",
    "export-job",
)

ID_PATTERN = r"^[a-z][a-z0-9-]{2,63}$"
SHA256_PATTERN = r"^[a-f0-9]{64}$"


def content_schema() -> dict[str, Any]:
    """Retorna o shape compartilhado de texto clínico e alergias."""
    return {
        "type": "object",
        "properties": {
            "chief_complaint": {"type": ["string", "null"]},
            "history": {"type": ["string", "null"]},
            "observations": {"type": ["string", "null"]},
            "assessment": {"type": ["string", "null"]},
            "plan": {"type": ["string", "null"]},
            "allergy_status": {
                "type": "string",
                "enum": ["not_recorded", "none_reported", "known"],
            },
            "allergy_details": {"type": ["string", "null"]},
        },
        "required": [
            "chief_complaint",
            "history",
            "observations",
            "assessment",
            "plan",
            "allergy_status",
            "allergy_details",
        ],
        "additionalProperties": False,
        "allOf": [
            {
                "if": {
                    "properties": {"allergy_status": {"const": "known"}},
                    "required": ["allergy_status"],
                },
                "then": {
                    "properties": {
                        "allergy_details": {"type": "string", "minLength": 1}
                    }
                },
            },
            {
                "if": {
                    "properties": {
                        "allergy_status": {"enum": ["not_recorded", "none_reported"]}
                    },
                    "required": ["allergy_status"],
                },
                "then": {"properties": {"allergy_details": {"const": None}}},
            },
        ],
    }


def base_schema(title: str, schema_id: str, properties: dict[str, Any], required: list[str]) -> dict[str, Any]:
    """Monta um schema standalone Draft 2020-12 com objeto fechado."""
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"https://spec-foundry.example/prontuario-simples/{schema_id}.schema.json",
        "title": title,
        "type": "object",
        "properties": properties,
        "required": required,
        "additionalProperties": False,
    }


def schema_documents() -> dict[str, dict[str, Any]]:
    """Retorna todos os sete schemas de domínio, sem ler ou alterar o modelo genérico."""
    content_ref = {"$ref": "#/$defs/content"}
    schemas: dict[str, dict[str, Any]] = {}

    schemas["patient"] = base_schema(
        "Patient snapshot v0.1",
        "patient",
        {
            "schema_version": {"const": SCHEMA_VERSION},
            "id": {"type": "string", "pattern": ID_PATTERN},
            "clinic_id": {"type": "string", "pattern": ID_PATTERN},
            "local_number": {"type": "string", "minLength": 1},
            "full_name": {"type": "string", "minLength": 1},
            "birth_date": {"type": "string", "format": "date"},
            "preferred_name": {"type": ["string", "null"], "minLength": 1},
            "version": {"type": "integer", "minimum": 1},
            "status": {"type": "string", "enum": ["active", "inactive"]},
        },
        [
            "schema_version",
            "id",
            "clinic_id",
            "local_number",
            "full_name",
            "birth_date",
            "preferred_name",
            "version",
            "status",
        ],
    )

    schemas["draft-command"] = base_schema(
        "Draft command v0.1",
        "draft-command",
        {
            "encounter_id": {"type": "string", "pattern": ID_PATTERN},
            "expected_version": {"type": "integer", "minimum": 1},
            "content": content_ref,
        },
        ["encounter_id", "expected_version", "content"],
    )
    schemas["draft-command"]["$defs"] = {"content": content_schema()}

    schemas["finalize-command"] = base_schema(
        "Finalize command v0.1",
        "finalize-command",
        {
            "expected_version": {"type": "integer", "minimum": 1},
            "idempotency_key": {"type": "string", "minLength": 16},
        },
        ["expected_version", "idempotency_key"],
    )

    schemas["record-snapshot"] = base_schema(
        "Finalized record snapshot v0.1",
        "record-snapshot",
        {
            "schema_version": {"const": SCHEMA_VERSION},
            "id": {"type": "string", "pattern": ID_PATTERN},
            "clinic_id": {"type": "string", "pattern": ID_PATTERN},
            "patient_id": {"type": "string", "pattern": ID_PATTERN},
            "encounter_id": {"type": "string", "pattern": ID_PATTERN},
            "author_id": {"type": "string", "pattern": ID_PATTERN},
            "professional_registration": {
                "type": "object",
                "properties": {
                    "council": {"type": "string", "minLength": 1},
                    "region": {"type": "string", "minLength": 1},
                    "number": {"type": "string", "minLength": 1},
                },
                "required": ["council", "region", "number"],
                "additionalProperties": False,
            },
            "patient_identity": {
                "type": "object",
                "properties": {
                    "full_name": {"type": "string", "minLength": 1},
                    "birth_date": {"type": "string", "format": "date"},
                    "local_number": {"type": "string", "minLength": 1},
                },
                "required": ["full_name", "birth_date", "local_number"],
                "additionalProperties": False,
            },
            "encounter_at": {"type": "string", "format": "date-time"},
            "finalized_at": {"type": "string", "format": "date-time"},
            "version": {"type": "integer", "minimum": 1},
            "status": {"const": "finalized"},
            "content": content_ref,
            "content_sha256": {"type": "string", "pattern": SHA256_PATTERN},
            "canonicalization_version": {"const": CANONICALIZATION_VERSION},
            "signature_status": {"const": "not_implemented"},
        },
        [
            "schema_version",
            "id",
            "clinic_id",
            "patient_id",
            "encounter_id",
            "author_id",
            "professional_registration",
            "patient_identity",
            "encounter_at",
            "finalized_at",
            "version",
            "status",
            "content",
            "content_sha256",
            "canonicalization_version",
            "signature_status",
        ],
    )
    schemas["record-snapshot"]["$defs"] = {"content": content_schema()}

    schemas["addendum-command"] = base_schema(
        "Addendum command v0.1",
        "addendum-command",
        {
            "snapshot_id": {"type": "string", "pattern": ID_PATTERN},
            "reason": {"type": "string", "minLength": 1},
            "text": {"type": "string", "minLength": 1},
            "idempotency_key": {"type": "string", "minLength": 1},
        },
        ["snapshot_id", "reason", "text", "idempotency_key"],
    )

    schemas["attachment"] = base_schema(
        "Attachment snapshot v0.1",
        "attachment",
        {
            "schema_version": {"const": SCHEMA_VERSION},
            "id": {"type": "string", "pattern": ID_PATTERN},
            "clinic_id": {"type": "string", "pattern": ID_PATTERN},
            "patient_id": {"type": "string", "pattern": ID_PATTERN},
            "encounter_id": {"type": "string", "pattern": ID_PATTERN},
            "storage_key": {
                "type": "string",
                "pattern": r"^private/[a-f0-9]{2}/[a-f0-9]{64}$",
            },
            "media_type": {"type": "string", "enum": ["application/pdf", "image/jpeg", "image/png"]},
            "bytes": {"type": "integer", "minimum": 1},
            "sha256": {"type": "string", "pattern": SHA256_PATTERN},
            "status": {"type": "string", "enum": ["quarantined", "clean", "rejected", "scan_failed"]},
            "scan_engine_version": {"type": ["string", "null"], "minLength": 1},
            "scanned_at": {"type": ["string", "null"], "format": "date-time"},
        },
        [
            "schema_version",
            "id",
            "clinic_id",
            "patient_id",
            "encounter_id",
            "storage_key",
            "media_type",
            "bytes",
            "sha256",
            "status",
            "scan_engine_version",
            "scanned_at",
        ],
    )
    schemas["attachment"]["allOf"] = [
        {
            "if": {"properties": {"status": {"const": "clean"}}, "required": ["status"]},
            "then": {
                "properties": {
                    "scan_engine_version": {"type": "string", "minLength": 1},
                    "scanned_at": {"type": "string", "format": "date-time"},
                }
            },
        }
    ]

    schemas["export-job"] = base_schema(
        "Export job snapshot v0.1",
        "export-job",
        {
            "schema_version": {"const": SCHEMA_VERSION},
            "id": {"type": "string", "pattern": ID_PATTERN},
            "clinic_id": {"type": "string", "pattern": ID_PATTERN},
            "patient_id": {"type": "string", "pattern": ID_PATTERN},
            "requested_by": {"type": "string", "pattern": ID_PATTERN},
            "copy_request_id": {"type": "string", "pattern": ID_PATTERN},
            "status": {
                "type": "string",
                "enum": ["pending", "generating", "ready", "failed", "expired"],
            },
            "snapshot_ids": {
                "type": "array",
                "items": {"type": "string", "pattern": ID_PATTERN},
                "minItems": 1,
                "uniqueItems": True,
            },
            "attachment_ids": {
                "type": "array",
                "items": {"type": "string", "pattern": ID_PATTERN},
                "uniqueItems": True,
            },
            "expires_at": {"type": ["string", "null"], "format": "date-time"},
        },
        [
            "schema_version",
            "id",
            "clinic_id",
            "patient_id",
            "requested_by",
            "copy_request_id",
            "status",
            "snapshot_ids",
            "attachment_ids",
            "expires_at",
        ],
    )

    return schemas


def canonical_content_bytes(content: dict[str, Any]) -> bytes:
    """Serializa ``content`` exatamente como definido por content-json-v1."""
    return json.dumps(
        content,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def content_sha256(content: dict[str, Any]) -> str:
    """Calcula o digest dos bytes canônicos do conteúdo, nunca de autoria."""
    return hashlib.sha256(canonical_content_bytes(content)).hexdigest()


def example_documents() -> dict[str, dict[str, Any]]:
    """Retorna fixtures determinísticas, fictícias e sem CPF/telefone/dados reais."""
    content = {
        "chief_complaint": "Registro fictício para testar salvamento; sem validade clínica",
        "history": None,
        "observations": None,
        "assessment": None,
        "plan": None,
        "allergy_status": "not_recorded",
        "allergy_details": None,
    }
    return {
        "patient": {
            "schema_version": SCHEMA_VERSION,
            "id": "pat-demo-a",
            "clinic_id": "clinic-demo",
            "local_number": "LOCAL-0001",
            "full_name": "Pessoa Fictícia A",
            "birth_date": "1990-05-12",
            "preferred_name": None,
            "version": 1,
            "status": "active",
        },
        "draft-command": {
            "encounter_id": "enc-demo-a-001",
            "expected_version": 1,
            "content": content,
        },
        "finalize-command": {
            "expected_version": 1,
            "idempotency_key": "idem-demo-finalize-0001",
        },
        "record-snapshot": {
            "schema_version": SCHEMA_VERSION,
            "id": "snap-demo-a-001",
            "clinic_id": "clinic-demo",
            "patient_id": "pat-demo-a",
            "encounter_id": "enc-demo-a-001",
            "author_id": "usr-demo-clinician",
            "professional_registration": {
                "council": "CRM",
                "region": "SP",
                "number": "000000-FICT",
            },
            "patient_identity": {
                "full_name": "Pessoa Fictícia A",
                "birth_date": "1990-05-12",
                "local_number": "LOCAL-0001",
            },
            "encounter_at": "2026-11-10T10:00:00-03:00",
            "finalized_at": "2026-11-10T10:05:00-03:00",
            "version": 1,
            "status": "finalized",
            "content": content,
            "content_sha256": content_sha256(content),
            "canonicalization_version": CANONICALIZATION_VERSION,
            "signature_status": "not_implemented",
        },
        "addendum-command": {
            "snapshot_id": "snap-demo-a-001",
            "reason": "Correção administrativa fictícia",
            "text": "Aditivo fictício sem validade clínica.",
            "idempotency_key": "idem-demo-addendum-0001",
        },
        "attachment": {
            "schema_version": SCHEMA_VERSION,
            "id": "att-demo-a-001",
            "clinic_id": "clinic-demo",
            "patient_id": "pat-demo-a",
            "encounter_id": "enc-demo-a-001",
            "storage_key": "private/7f/7f2c4d8a6b1e3f905a7c9d2e4b6f8a0c1d3e5f7092b4c6d8e0f1a3b5c7d9e1f3",
            "media_type": "application/pdf",
            "bytes": 128,
            "sha256": "6c5c4e3d2b1a0987654321fedcba0123456789abcdef0123456789abcdef0123",
            "status": "clean",
            "scan_engine_version": "synthetic-scan-1",
            "scanned_at": "2026-11-10T10:06:00-03:00",
        },
        "export-job": {
            "schema_version": SCHEMA_VERSION,
            "id": "export-demo-a-001",
            "clinic_id": "clinic-demo",
            "patient_id": "pat-demo-a",
            "requested_by": "usr-demo-clinician",
            "copy_request_id": "copy-demo-001",
            "status": "ready",
            "snapshot_ids": ["snap-demo-a-001"],
            "attachment_ids": ["att-demo-a-001"],
            "expires_at": "2026-11-11T00:00:00-03:00",
        },
    }


def write_json(path: Path, value: Any) -> None:
    """Escreve JSON UTF-8 estável, com newline final."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def build(root: Path = ROOT) -> tuple[list[Path], list[Path]]:
    """Gera os 7 schemas e 7 examples; não altera ``project-model.schema.json``."""
    schemas_dir = root / "schemas"
    examples_dir = root / "examples"
    schemas = schema_documents()
    examples = example_documents()
    schema_paths: list[Path] = []
    example_paths: list[Path] = []
    for name in SCHEMA_NAMES:
        schema_path = schemas_dir / f"{name}.schema.json"
        example_path = examples_dir / f"{name}.example.json"
        write_json(schema_path, schemas[name])
        write_json(example_path, examples[name])
        schema_paths.append(schema_path)
        example_paths.append(example_path)
    return schema_paths, example_paths


def main() -> int:
    schema_paths, example_paths = build()
    print(f"GERADO — domain_contracts v{SCHEMA_VERSION}")
    print(f"Schemas: {len(schema_paths)}")
    print(f"Examples: {len(example_paths)}")
    print("Offline determinístico; sem LLM/rede; project-model.schema.json preservado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
