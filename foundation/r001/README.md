# Prontuário simples — fundação spec/eval r001

Pacote para um iniciante construir com assistência de IA um registro clínico ambulatorial simples. **É uma fundação proposta, não um aplicativo, prontuário certificado ou autorização para atender pacientes.** Estado: discovery. Profissão, especialidade, clínica, orçamento, assinatura, operação e responsáveis precisam de resposta humana.

## Comece sem tentar fazer tudo

1. Leia o [guia para o amigo iniciante](docs/START-HERE.md).
2. Mostre ao parceiro clínico as [perguntas essenciais](docs/open-questions.md), o [recorte do produto](docs/specs/01-product-spec.md) e os [limites de saúde e privacidade](docs/regulatory-and-clinical-boundaries.md).
3. Planeje a primeira tarefa do [backlog](docs/specs/04-implementation-plan.md), só com dados fictícios.
4. Use [AGENTS.md](AGENTS.md) e [CLAUDE.md](CLAUDE.md) como instruções para a IA, sem pedir o sistema inteiro de uma vez.

## Recomendação

Uma clínica por implantação, consultório ambulatorial adulto como hipótese inicial. Contas individuais, recepção/administrador/profissional com permissões próprias. Cadastro → agenda → atendimento manual → rascunho → snapshot fechado → adendo/histórico → cópia controlada.

Django LTS + templates + PostgreSQL; auth/MFA por bibliotecas homologadas e anexos privados. Sem SPA/microserviços no começo. Não há código de Django ou infraestrutura neste ZIP; apenas scripts offline de contratos e validação. Não escolhemos plano cloud nem configuramos banco/storage/segredos.

**Fora da v1:** IA clínica/transcrição, receitas/atestados, cálculo de dose, telemedicina, financeiro/convênios, integrações, hospital e offline com sincronização. O mínimo de segurança não é opcional: paciente correto, permissão no servidor, histórico íntegro, backup restaurável e revisão profissional antes de uso real.

## Pesquisa

[Benchmark e recomendação](docs/benchmark-and-scope.md) de iClinic, Feegow Clinic, Amplimed, Ninsaúde Clinic e HiDoctor, a partir de páginas oficiais de produto/suporte. Funcionalidade anunciada não equivale a auditoria de conformidade, disponibilidade em todo plano ou teste de uso. São referências de capacidade, não clones de interface/código.

Pesquisa normativa consultada em 10/11/2026: LGPD, Lei 13.787/2018, Estatuto dos Direitos do Paciente de 2026, normas/pareceres CFM e orientação Anvisa/ANPD. A profissão ainda não definida limita a aplicabilidade; não presumir que regras médicas sejam universais. Referências e cautelas estão em [limites clínicos](docs/regulatory-and-clinical-boundaries.md).

## Documentação de implementação

- [01 Produto](docs/specs/01-product-spec.md), [02 Requisitos](docs/specs/02-requirements.md), [03 Desenho](docs/specs/03-system-design.md), [04 Plano](docs/specs/04-implementation-plan.md), [05 Configuração de agentes](docs/specs/05-agent-configuration.md).
- [Domínio](docs/domain-model.md), [contratos](docs/data-contracts.md), [operações futuras](docs/application-commands.md), [telas e estados](docs/ux-and-screen-contracts.md), [ADRs propostas](docs/adr/README.md).
- [Rastreabilidade](docs/traceability.md), [perguntas](docs/open-questions.md), [riscos](docs/assumptions-and-risks.md), [revisão](docs/review.md), [impacto](docs/change-impact.md).
- [Eval specs](evals/eval-spec.md), [casos](evals/cases.json) e [rubricas](evals/rubrics.md). Todos os 34 casos do aplicativo começam não executados/bloqueados.

`model/project-model.json` é o snapshot canônico do pacote. `schemas/` e `examples/` contêm contratos propostos de domínio com dados fictícios. Nenhuma fixture é prontuário real ou gold clínico. A ficha final não pode ser validada só porque JSON Schema aceitou os campos.

## Verificação local

Python 3.11+; Python 3.12 é referência de desenvolvimento. Em pasta extraída, use:

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python scripts/check_foundation.py
```

O comando verifica arquivos, contratos/exemplos, links locais e testes offline. Em exportação, verifica também o manifest e os hashes. **Não executa aplicativo, autenticação, permissões HTTP, scan de malware, assinatura, backup remoto ou atendimento clínico.** O relatório `evals/reports/local-checks.json` registra o alcance real da execução. Nenhum caso target_system vira passed por esse comando.

Os scripts `build_project_model.py` e `build_domain_contracts.py` são fontes determinísticas desta r001. Não regenerar uma revisão já aprovada ou seus relatórios sem plano de atualização: eles recriam exemplos/estado inicial. Para manutenção autorizada de r001 em discovery, depois da regeneração use `register_artifacts.py`, check e export com novo manifest. Preservar snapshots aprovados em r002 etc.

## Entrega e integridade

O ZIP inclui somente artefatos registrados e um `manifest.json` com hashes. Originais locais em `sources/`, caches, segredos e dados privados não entram. Fontes públicas estão referenciadas por URL; disponibilidade e texto podem mudar. Manifest não autentica autor, assinatura ou aprovação clínica. Os validadores portáteis acompanham o pacote para outra IA repetir os checks após extrair.

## Próximo passo concreto

Seu amigo não precisa escolher todas as funcionalidades dos concorrentes. Precisa primeiro entender uma consulta do início ao fim com um profissional da área e ter apoio técnico para os controles críticos. TASK-001/002 definem essa base. A jornada sintética pode avançar depois do recorte acordado; usar pacientes reais depende dos gates da TASK-014/015, não de “a tela já estar pronta”.
