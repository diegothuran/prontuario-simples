"""Atualiza allowlist da fundação em discovery; não publica e não faz scanner DLP."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    p = ROOT / 'model/project-model.json'
    model = json.loads(p.read_text(encoding='utf-8'))
    if model['readiness'] != 'discovery':
        raise SystemExit('Baseline não está em discovery; crie revisão explícita antes de registrar.')
    excluded = {'sources', '.git', '.venv', '__pycache__', '.pytest_cache', 'node_modules', 'dist'}
    suffixes = {'.md', '.py', '.json', '.txt'}
    files = []
    for path in sorted(ROOT.rglob('*')):
        relative = path.relative_to(ROOT)
        if any(part in excluded for part in relative.parts) or path.name == 'manifest.json':
            continue
        if path.is_symlink():
            raise ValueError('Symlink não permitido: ' + str(relative))
        if path.is_file() and (path.suffix in suffixes or path.name == '.gitignore'):
            if path.suffix in {'.pem', '.key', '.p12', '.pfx'} or path.name.startswith('.env'):
                raise ValueError('Segredo fora de escopo: ' + str(relative))
            files.append({'path':relative.as_posix(),'requirement_refs':[],'eval_refs':[]})
    # A tabela de rastreabilidade contém todos os requisitos/casos do target.
    for a in files:
        if a['path'] == 'docs/specs/02-requirements.md':
            a['requirement_refs'] = [r['id'] for r in model['requirements']]
        if a['path'] == 'docs/traceability.md':
            a['requirement_refs'] = [r['id'] for r in model['requirements']]
            a['eval_refs'] = [e['id'] for e in model['eval_cases']]
    model['artifacts'] = files
    p.write_text(json.dumps(model,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Artefatos registrados:',len(files),'; sources/ não será exportado. Revisar conteúdo continua necessário.')


if __name__ == '__main__':
    main()
