#!/usr/bin/env python3
"""Valida contratos/referências locais; não aprova semântica nem executa sistema-alvo."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
from common import dump, validate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True)
    parser.add_argument('--report', help='Salvar JSON de checks locais em arquivo novo')
    parser.add_argument('--exported', action='store_true', help='Verificar pacote exportado sem exigir originais privados excluídos')
    args = parser.parse_args()
    result = validate(Path(args.project), exported=args.exported)
    result['scope'] = 'local_contract_checks'
    result['checked_at'] = datetime.now(timezone.utc).isoformat()
    if args.report:
        report = Path(args.report)
        if report.exists():
            parser.error('Relatório já existe; usar arquivo novo')
        report.parent.mkdir(parents=True, exist_ok=True)
        dump(report, result)
    print(result['structural_status'].upper(), '— local_contract_checks')
    for message in result['errors']:
        print('ERRO:', message)
    for message in result.get('warnings', []):
        print('AVISO:', message)
    print('Estado declarado:', result.get('declared_readiness', 'não validado'))
    print('Não é grounding, aprovação autenticada ou execução de evals do sistema-alvo.')
    raise SystemExit(0 if result['structural_status'] == 'pass' else 1)


if __name__ == '__main__':
    main()
