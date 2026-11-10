# Verificação da fundação r001

Execução offline em 10/11/2026. O relatório detalhado está em [evals/reports/local-checks.json](../evals/reports/local-checks.json). A pesquisa comparou cinco fornecedores por fontes públicas oficiais de produto/suporte, sem login ou auditoria técnica de seus sistemas.

## Executado

- Sete JSON Schemas de domínio e sete examples fictícios: metacheck Draft 2020-12, validação com FormatChecker e invariantes locais.
- Modelo canônico: schema, IDs/referências, estados propostos/discovery, rastreabilidade, links locais e allowlist de artefatos.
- 23 testes unitários offline: 14 contratos de domínio e 9 checks de fundação, incluindo casos negativos de autoridade no input, hash/tempo, vínculo sintético, clínica divergente, falsificação de execução/prontidão/aceite, referência inexistente e ciclo de tarefas.
- Parsing da sintaxe dos scripts/tests Python sem chamar rede ou criar aplicação.
- Exportação com manifest/hashes; cópia extraída é revalidada com os mesmos comandos. Originais em sources/ não fazem parte da entrega.

O relatório da execução local registra `layer: package` e `target_system_cases_executed: 0`. Os 34 cenários do produto não foram executados: 32 not_run e 2 blocked. Nenhuma revisão clínica/aceite da baseline está autenticada ou registrada como aprovação.

## Não executado

Aplicativo Django, login/MFA, APIs/policies por objeto, navegação de UI, concorrência PostgreSQL, scanner real, storage privado, export clínico em PDF/JSON, assinatura/provedor, restore de backup, revisão profissional da ficha, avaliação de acessibilidade de implementação, pentest, implantação e operação com pacientes. Nomes, datas, hashes e `clean/ready` nas fixtures não provam esses resultados.

## Interpretação correta

Pode usar esta fundação para planejar e iniciar tarefas autorizadas em ambiente fictício. Não pode dizer que o prontuário está funcionando, certificado, seguro para todos os cenários ou aprovado para atendimento. Questões bloqueadoras estão em [open-questions.md](open-questions.md). Produção requer decisões e evidências do release verdadeiro.
