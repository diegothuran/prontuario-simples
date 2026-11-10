"""Validação offline não mutante por padrão. --report grava resultado, não executa target."""
import argparse
import ast
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from common import validate

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser(description='Confere a fundação/contratos; não liga aplicação ou pacientes.')
    parser.add_argument('--report',help='Caminho de relatório. Se gravar dentro do pacote, registrar novamente e reconstruir manifest antes de exportar.')
    args=parser.parse_args()
    env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    exported=(ROOT/'manifest.json').exists()
    package=validate(ROOT,exported=exported)
    syntax=[]
    for base in ('scripts','tests'):
        for p in sorted((ROOT/base).rglob('*.py')):
            ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
            syntax.append(p.relative_to(ROOT).as_posix())
    commands=[
        [sys.executable,str(ROOT/'scripts/check_domain_contracts.py')],
        [sys.executable,'-m','unittest','discover','-s',str(ROOT/'tests'),'-v'],
    ]
    outcomes=[]
    for cmd in commands:
        run=subprocess.run(cmd,cwd=ROOT,env=env,text=True,capture_output=True)
        outcomes.append({'command': [Path(c).name if c==sys.executable else c.replace(str(ROOT),'PROJECT') for c in cmd], 'returncode':run.returncode,'stdout':run.stdout,'stderr':run.stderr})
        print(run.stdout,end='')
        if run.stderr:
            print(run.stderr,end='',file=sys.stderr)
    passed=package['structural_status']=='pass' and all(o['returncode']==0 for o in outcomes)
    result={'layer':'package','revision':'r001','executed_at':datetime.now(timezone.utc).isoformat(),'status':'passed' if passed else 'failed','executor':'scripts/check_foundation.py','scope':'Local structural/contract checks only','structural_result':package,'python_syntax_checked':syntax,'commands':outcomes,'target_system_cases_executed':0,'limitations':['Não executa o prontuário, login/MFA, policies HTTP, scanner, assinatura ou restore.','Não comprova conformidade legal ou segurança clínica.','Matriz sintética e hashes não são gold médico, assinatura ou autenticação.','Fontes públicas referenciadas por URL foram consultadas; este comando não faz pesquisa nem autentica fontes.']}
    print('Fundação offline:',result['status'],'| Target executado: 0 | Readiness:',package.get('declared_readiness'))
    if package.get('errors'):
        print(json.dumps(package['errors'],ensure_ascii=False,indent=2))
    if args.report:
        out=Path(args.report).resolve()
        out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print('Relatório gravado; se ele estiver dentro da fundação, atualizar registro e manifest para exportação.')
    return 0 if passed else 1


if __name__=='__main__':
    raise SystemExit(main())
