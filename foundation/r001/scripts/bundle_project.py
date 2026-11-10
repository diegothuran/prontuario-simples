#!/usr/bin/env python3
"""Exporta artefatos registrados, sem originais privados. Não prova autenticidade."""
import argparse
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from common import SKILL_ROOT, digest, dump, load, safe_path, validate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    root = Path(args.project).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    if output.exists() or output.is_relative_to(root) or output.is_relative_to(SKILL_ROOT):
        parser.error('ZIP precisa ser novo e externo ao projeto/skill')
    if (root/'manifest.json').exists():
        parser.error('Manifest já existe; preservar snapshot e usar nova revisão/pasta para alterar')
    result = validate(root)
    if result['structural_status'] != 'pass':
        for error in result['errors']:
            print('ERRO:', error)
        raise SystemExit(1)
    model = load(root/'model/project-model.json')
    paths = sorted(artifact['path'] for artifact in model['artifacts'])
    files = [{'path': name, 'sha256': digest(safe_path(root, name)), 'bytes': safe_path(root, name).stat().st_size} for name in paths]
    manifest = {
        'purpose': 'generated_project_bundle', 'skill_version': '1.0.0',
        'project_id': model['project_id'], 'revision': model['revision'], 'scope': model['scope'],
        'declared_readiness': model['readiness'], 'created_at': datetime.now(timezone.utc).isoformat(),
        'structural_check': result, 'files': files, 'private_original_sources_included': False,
        'approval_records_are_declarations_not_authenticated': True,
        'target_system_tests_executed_by_exporter': False,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    dump(root/'manifest.json', manifest)
    try:
        with zipfile.ZipFile(output, 'x', zipfile.ZIP_DEFLATED) as z:
            for name in paths + ['manifest.json']:
                z.write(safe_path(root, name), f"{model['project_id']}-{model['revision']}/{name}")
        with zipfile.ZipFile(output) as z:
            if z.testzip() is not None:
                raise ValueError('Erro de integridade ZIP')
    except Exception:
        output.unlink(missing_ok=True)
        (root/'manifest.json').unlink(missing_ok=True)
        raise
    print(f'Pacote exportado: {output}')
    print(f"Estado declarado: {model['readiness']}; originais privados excluídos.")
    print('O destinatário pode verificar com validate_package.py --exported; grounding continua revisão externa.')


if __name__ == '__main__':
    main()
