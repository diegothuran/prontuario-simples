#!/usr/bin/env python3
"""Testes offline dos contratos de domínio v0.1.

Os testes exercitam schemas e invariantes sintéticas de fixtures. Não são
permission policy runtime, não testam endpoints, não autenticam autoria,
não provam isolamento de tenant, assinatura legal, integridade externa,
validade clínica ou cadastro médico normativo.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_domain_contracts import (  # noqa: E402
    SCHEMA_NAMES,
    build,
    canonical_content_bytes,
    content_sha256,
    example_documents,
    schema_documents,
)
from check_domain_contracts import (  # noqa: E402
    FIXTURE_NOW,
    load_contracts,
    run_checks,
    schema_errors,
    validate_invariants,
    validate_positive_examples,
)


class DomainContractTests(unittest.TestCase):
    """Valida contratos locais; não substitui testes de aplicação ou segurança."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.schemas, cls.examples = load_contracts(ROOT)

    def assertSchemaValid(self, name: str, instance: dict) -> None:
        self.assertEqual([], schema_errors(name, instance, self.schemas[name]))

    def assertSchemaInvalid(self, name: str, instance: dict) -> None:
        self.assertTrue(schema_errors(name, instance, self.schemas[name]), f"esperava rejeição: {name}")

    def test_all_examples_validate_against_matching_schemas(self) -> None:
        """Todos os pares positivos usam Draft202012Validator + FormatChecker."""
        self.assertEqual([], validate_positive_examples(self.schemas, self.examples))
        self.assertEqual(set(SCHEMA_NAMES), set(self.schemas))
        self.assertEqual(set(SCHEMA_NAMES), set(self.examples))

    def test_fixture_relationships_and_invariants_pass(self) -> None:
        self.assertEqual([], validate_invariants(self.examples))
        result = run_checks(ROOT)
        self.assertEqual("pass", result["status"])
        self.assertEqual(7, result["schema_count"])
        self.assertEqual(7, result["example_count"])
        self.assertTrue(result["limitations"])
        self.assertEqual(FIXTURE_NOW.isoformat(), result["fixture_now"])

    def test_build_is_deterministic_and_only_writes_contract_outputs(self) -> None:
        """A geração em diretórios temporários é estável e não inclui o modelo genérico."""
        with tempfile.TemporaryDirectory() as first_dir, tempfile.TemporaryDirectory() as second_dir:
            first_root = Path(first_dir)
            second_root = Path(second_dir)
            first_schemas, first_examples = build(first_root)
            second_schemas, second_examples = build(second_root)
            first_bytes = [path.read_bytes() for path in first_schemas + first_examples]
            second_bytes = [path.read_bytes() for path in second_schemas + second_examples]
            self.assertEqual(first_bytes, second_bytes)
            self.assertFalse((first_root / "schemas" / "project-model.schema.json").exists())
            self.assertFalse((first_root / "model" / "project-model.json").exists())

    def test_canonical_hash_is_content_only_and_python_labeled(self) -> None:
        snapshot = copy.deepcopy(self.examples["record-snapshot"])
        expected = hashlib.sha256(
            json.dumps(
                snapshot["content"],
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        self.assertEqual(expected, content_sha256(snapshot["content"]))
        self.assertEqual(expected, snapshot["content_sha256"])
        self.assertEqual(
            canonical_content_bytes(snapshot["content"]),
            json.dumps(snapshot["content"], ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"),
        )

    def test_forged_author_tenant_and_status_are_rejected_from_client_commands(self) -> None:
        """Campos derivados rejeitados são contrato fechado, não uma policy de autorização."""
        draft = copy.deepcopy(self.examples["draft-command"])
        draft.update({"author_id": "usr-forged", "clinic_id": "clinic-forged", "patient_id": "pat-forged", "status": "finalized"})
        self.assertSchemaInvalid("draft-command", draft)

        finalize = copy.deepcopy(self.examples["finalize-command"])
        finalize.update({"author_id": "usr-forged", "clinic_id": "clinic-forged", "status": "finalized", "content": {}})
        self.assertSchemaInvalid("finalize-command", finalize)

        addendum = copy.deepcopy(self.examples["addendum-command"])
        addendum.update({"author_id": "usr-forged", "clinic_id": "clinic-forged", "status": "finalized"})
        self.assertSchemaInvalid("addendum-command", addendum)

    def test_bad_snapshot_hash_is_rejected_by_schema_invariant(self) -> None:
        snapshot = copy.deepcopy(self.examples["record-snapshot"])
        snapshot["content_sha256"] = "0" * 64
        self.assertSchemaValid("record-snapshot", snapshot)
        errors = validate_invariants({**self.examples, "record-snapshot": snapshot})
        self.assertTrue(any("content_sha256" in error for error in errors))

    def test_naive_timestamp_is_rejected(self) -> None:
        snapshot = copy.deepcopy(self.examples["record-snapshot"])
        snapshot["encounter_at"] = "2026-11-10T10:00:00"
        self.assertSchemaInvalid("record-snapshot", snapshot)
        errors = validate_invariants({**self.examples, "record-snapshot": snapshot})
        self.assertTrue(any("timezone-aware" in error for error in errors))

    def test_invalid_finalization_version_is_rejected(self) -> None:
        finalize = copy.deepcopy(self.examples["finalize-command"])
        finalize["expected_version"] = 0
        self.assertSchemaInvalid("finalize-command", finalize)
        errors = validate_invariants({**self.examples, "finalize-command": finalize})
        self.assertTrue(any("expected_version" in error for error in errors))

    def test_known_allergy_without_details_is_rejected(self) -> None:
        snapshot = copy.deepcopy(self.examples["record-snapshot"])
        snapshot["content"]["allergy_status"] = "known"
        snapshot["content"]["allergy_details"] = None
        self.assertSchemaInvalid("record-snapshot", snapshot)
        errors = validate_invariants({**self.examples, "record-snapshot": snapshot})
        self.assertTrue(any("allergy_status=known" in error for error in errors))

    def test_clean_attachment_without_scan_metadata_is_rejected(self) -> None:
        attachment = copy.deepcopy(self.examples["attachment"])
        attachment["scan_engine_version"] = None
        attachment["scanned_at"] = None
        self.assertSchemaInvalid("attachment", attachment)

    def test_public_url_is_rejected(self) -> None:
        attachment = copy.deepcopy(self.examples["attachment"])
        attachment["public_url"] = "https://example.invalid/private.pdf"
        self.assertSchemaInvalid("attachment", attachment)

        export_job = copy.deepcopy(self.examples["export-job"])
        export_job["public_url"] = "https://example.invalid/export.zip"
        self.assertSchemaInvalid("export-job", export_job)

    def test_mismatched_fixture_clinic_is_rejected_by_invariant(self) -> None:
        attachment = copy.deepcopy(self.examples["attachment"])
        attachment["clinic_id"] = "clinic-other"
        self.assertSchemaValid("attachment", attachment)
        examples = {**self.examples, "attachment": attachment}
        errors = validate_invariants(examples)
        self.assertTrue(any("attachment/patient clinic_id" in error for error in errors))

    def test_snapshot_cannot_be_draft_and_finalization_cannot_precede_encounter(self) -> None:
        snapshot = copy.deepcopy(self.examples["record-snapshot"])
        snapshot["status"] = "draft"
        self.assertSchemaInvalid("record-snapshot", snapshot)

        snapshot = copy.deepcopy(self.examples["record-snapshot"])
        snapshot["finalized_at"] = "2026-11-10T09:59:59-03:00"
        self.assertSchemaValid("record-snapshot", snapshot)
        errors = validate_invariants({**self.examples, "record-snapshot": snapshot})
        self.assertTrue(any("anterior a encounter_at" in error for error in errors))

        snapshot = copy.deepcopy(self.examples["record-snapshot"])
        snapshot["encounter_at"] = "2026-11-10T12:00:01-03:00"
        snapshot["finalized_at"] = "2026-11-10T12:01:00-03:00"
        self.assertSchemaValid("record-snapshot", snapshot)
        errors = validate_invariants({**self.examples, "record-snapshot": snapshot})
        self.assertTrue(any("encounter_at não pode estar no futuro" in error for error in errors))

    def test_fixture_dob_and_ready_expiry_use_explicit_fixture_time(self) -> None:
        patient = copy.deepcopy(self.examples["patient"])
        patient["birth_date"] = "2026-11-11"
        self.assertSchemaValid("patient", patient)
        errors = validate_invariants({**self.examples, "patient": patient})
        self.assertTrue(any("birth_date não pode estar no futuro" in error for error in errors))

        export_job = copy.deepcopy(self.examples["export-job"])
        export_job["expires_at"] = FIXTURE_NOW.isoformat()
        self.assertSchemaValid("export-job", export_job)
        errors = validate_invariants({**self.examples, "export-job": export_job})
        self.assertTrue(any("ready precisa expirar" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
