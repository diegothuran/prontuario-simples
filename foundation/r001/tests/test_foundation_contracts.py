"""Somente checks documentais; não testa login, política clínica ou aplicação."""
import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from common import validate  # noqa: E402


class FoundationContracts(unittest.TestCase):
    def setUp(self):
        self.model = json.loads((ROOT/'model/project-model.json').read_text(encoding='utf-8'))

    def check_mutation(self, change, fragment):
        with tempfile.TemporaryDirectory() as d:
            destination = Path(d)/'project'
            shutil.copytree(ROOT,destination,ignore=shutil.ignore_patterns('__pycache__','.venv','.git','manifest.json'))
            model = copy.deepcopy(self.model)
            change(model)
            (destination/'model/project-model.json').write_text(json.dumps(model,ensure_ascii=False),encoding='utf-8')
            result = validate(destination)
            self.assertEqual(result['structural_status'],'fail')
            self.assertTrue(any(fragment in error for error in result['errors']),result['errors'])

    def test_formal_model_schema(self):
        schema = json.loads((ROOT/'schemas/project-model.schema.json').read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(self.model)

    def test_untouched_foundation(self):
        result = validate(ROOT, exported=(ROOT/'manifest.json').exists())
        self.assertEqual(result['structural_status'], 'pass', result['errors'])

    def test_target_evals_not_falsely_executed(self):
        self.assertEqual(len(self.model['eval_cases']),34)
        self.assertTrue(all(e['layer']=='target_system' and e['execution_status'] in {'not_run','blocked'} and e['executor'] is None and e['report_ref'] is None for e in self.model['eval_cases']))
        self.assertEqual(self.model['readiness'],'discovery')
        self.assertFalse(self.model['approvals'])

    def test_no_readiness_with_blockers(self):
        self.check_mutation(lambda m:m.update(readiness='ready_for_review'),'Prontidão incompatível')

    def test_no_accepted_requirement_without_approval(self):
        self.check_mutation(lambda m:m['requirements'][0].update(status='accepted'),'aceitação sem decisão')

    def test_no_cyclic_tasks(self):
        self.check_mutation(lambda m:m['tasks'][0].update(dependency_refs=[m['tasks'][0]['id']]),'Dependência cíclica')

    def test_no_result_without_execution_report(self):
        self.check_mutation(lambda m:m['eval_cases'][0].update(execution_status='passed'),'resultado sem executor/relatório')

    def test_no_unresolved_source_reference(self):
        self.check_mutation(lambda m:m['evidence'][0].update(source_ref='SRC-INVENTADA'),'referência não resolvida')

    def test_proposed_defaults_are_not_enforcement(self):
        cfg=json.loads((ROOT/'configs/proposed-defaults.json').read_text(encoding='utf-8'))
        self.assertTrue(cfg['not_runtime_enforcement'])
        for key in ['clinical_ai_enabled','prescription_enabled','telemedicine_enabled','physical_record_delete_enabled','offline_clinical_cache_enabled']:
            self.assertFalse(cfg[key])
        self.assertEqual(cfg['signature_status'],'not_implemented')
        self.assertEqual(cfg['real_patient_use'],'blocked_pending_homologation')


if __name__ == '__main__':
    unittest.main()
