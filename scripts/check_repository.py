"""Checks offline do repositório aberto; não executa prontuário, deploy ou pacientes."""
import ast
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

from jsonschema import FormatChecker

ROOT=Path(__file__).resolve().parents[1]


def main():
    required=['README.md','START-HERE.md','AGENTS.md','CLAUDE.md','CONTRIBUTING.md','SECURITY.md','LICENSE','requirements-dev.txt','docs/DEVELOPMENT.md','.github/workflows/checks.yml']
    errors=[]
    if FormatChecker().conforms('2026-01-01T12:00:00','date-time'):
        errors.append('Validador RFC3339 ausente/inadequado: instale requirements-dev.txt da raiz com o extra format-nongpl.')
    for name in required:
        p=ROOT/name
        if not p.is_file() or not p.read_text(encoding='utf-8').strip():
            errors.append('Arquivo obrigatório ausente/vazio: '+name)
    foundation=ROOT/'foundation/r001'
    manifest=json.loads((foundation/'manifest.json').read_text(encoding='utf-8'))
    for record in manifest['files']:
        rel=Path(record['path'])
        p=foundation/rel
        if rel.is_absolute() or '..' in rel.parts or p.is_symlink():
            errors.append('Caminho inválido no manifest: '+record['path'])
            continue
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=record['sha256']:
            errors.append('Snapshot alterado ou faltante: '+record['path'])
    if (foundation/'sources').exists():
        errors.append('Originais sources/ não devem estar na distribuição pública.')
    excluded={'.git','.venv','__pycache__','.pytest_cache','node_modules','dist'}
    for p in ROOT.rglob('*'):
        rel=p.relative_to(ROOT)
        if any(part in excluded for part in rel.parts):
            continue
        if p.is_symlink():
            errors.append('Symlink na distribuição: '+str(rel))
            continue
        if not p.is_file():
            continue
        if p.name.startswith('.env') and p.name!='.env.example' or p.suffix in {'.pem','.key','.p12','.pfx','.dump','.sqlite3'} or any(part in {'sources','private-data','uploads'} for part in rel.parts):
            errors.append('Arquivo potencialmente privado fora do escopo: '+str(rel))
        if p.suffix=='.py':
            try:
                ast.parse(p.read_text(encoding='utf-8'),filename=str(rel))
            except SyntaxError as exc:
                errors.append(str(exc))
        if p.suffix=='.md' and 'foundation' not in rel.parts:
            for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)',p.read_text(encoding='utf-8')):
                if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',link) or link.startswith('#'):
                    continue
                path=unquote(link.split('#')[0])
                target=(p.parent/path).resolve()
                if not target.is_relative_to(ROOT) or not target.exists():
                    errors.append('Link local inválido: '+str(rel)+' -> '+link)
    if errors:
        print('\n'.join('ERRO: '+e for e in errors))
        return 1
    result=subprocess.run([sys.executable,str(foundation/'scripts/check_foundation.py')],cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),check=False)
    if result.returncode:
        return result.returncode
    print('OK: snapshot e distribuição preservados; 23 testes offline; nenhum caso de aplicativo executado.')
    print('Este check não detecta todo dado pessoal/segredo nem comprova segurança clínica; revisão humana permanece necessária.')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
