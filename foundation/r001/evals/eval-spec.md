# Eval specs — prontuário simples r001

O arquivo [cases.json](cases.json) é a mesma lista de casos do ProjectModel: 34 cenários de sistema-alvo, inicialmente 32 `not_run` e 2 `blocked`. Não existe aplicativo clínico neste pacote. Fixtures sintéticas são matriz de cenários, não gold médico nem seed de banco de produção. Regeneração do modelo restaura esse estado de planejamento.

## Camadas que não podem ser misturadas

**Pacote/contratos locais:** schema, IDs/links, rastreabilidade, dados fictícios, invariantes de hash/estado e inputs fechados. `scripts/check_foundation.py` e testes locais verificam apenas esta camada. Relatório declara `layer: package`; não muda nenhum EVAL de produto para passed.

**Aplicação implementada:** navegador, sessões e MFA reais em ambiente de teste, policies por objeto, concorrência PostgreSQL, storage privado/scanner, proxy/export e audit. Mocks servem para UI, mas não comprovam integração. Mesmo teste que usa dados sintéticos pode ter infraestrutura real; identificar qual parte foi simulada.

**Validação profissional e operação:** adequação da ficha e dos fluxos à profissão, assinatura/preservação, privacy e suporte/backup/contingência. Uma IA que gerou o formulário não é o único juiz dele. Precisa responsável clínico e revisor técnico/privacidade apropriados.

Não há layer de avaliação de IA clínica, pois o produto não a inclui. Um futuro recurso de IA exigirá novo recorte, riscos, referências, gold/holdout e evals próprias; não reaproveitar aprovação de CRUD.

## Grupos e gate

- EVAL-001/006/032/034: delimitação de demo, adequação profissional e diferença entre fechamento e assinatura.
- EVAL-002/003/020/021/022: identidade, MFA, acesso e isolamento por objetos inclusive workers.
- EVAL-004/007/008/009/019/023/024/029: paciente correto, conteúdo, versões, corridas e correções atribuídas.
- EVAL-010/011/025/026: arquivos, cópia fiel, destinatário e revogação.
- EVAL-012/013/014/016/018/027/028/033: auditoria, retenção, observabilidade, restore e operação.
- EVAL-005/015/017/030/031: agenda, ausência de inferência clínica, exclusões, feedback e uso acessível.

Qualquer falha crítica impede liberação da função/uso correspondente. Casos críticos blocked também bloqueiam o gate em que são necessários; não entram como passed ou N/A. Isso não impede evoluir uma demo sintética claramente limitada. Nenhuma média de satisfação/coverage dilui vazamento, paciente errado, perda de nota ou assinatura inválida.

## Como executar depois

1. Registrar commit/release, revisão de specs, ambiente, versões DB/libs, papéis e infraestrutura simulada/real.
2. Provisionar fixtures fictícias e contas independentes. Não capturar snapshots de pacientes reais. Seeds de app deverão ser criados conforme modelo real, não importar JSON de domínio como tabela automaticamente.
3. Executar comportamento positivo e negativo; coletar HTTP, estado DB, sequência de UI, hashes/export/logs sem conteúdo sensível.
4. Revisor independente confere oracle e interpreta resultado. Clínico confere o modelo e fidelidade documental, não promete diagnósticos acertados por ausência de IA.
5. Reportar cada caso: passed/failed/blocked/not_run, motivo e evidência de execução. Atualizar modelo e cases juntos. Contrato de relatório do perfil Spec Foundry exige revision/layer/case_ids/status/executor/evidence_refs/limitations.
6. Decisão humana de release permanece separada dos testes. Mudar fornecedor, profissão ou assinatura invalida evidência afetada e exige reavaliação.

## Métricas e limiares propostos

Cobertura executada = (passed + failed) / total de casos aplicáveis, informando blocked/not_run e N/A separadamente. Taxa de aprovação = passed / (passed + failed), não dividir por casos planejados para inflar resultado. Também reportar falhas por severidade e casos críticos não executados.

Zero acessos indevidos, zero sobrescritas de finalized e nenhum paciente errado são critérios de aceitação nos cenários testados, não afirmação de risco zero universal. Recuperação: RPO/RTO só passam se medidos e aprovados contra targets escolhidos; snapshot JSON não testa restore. Não inventar taxa clínica, sensibilidade, especificidade ou retorno financeiro.

Performance preliminar a negociar: 95º percentil de busca/lista em até 2s no ambiente definido; fixture de 5.000 pacientes e 50.000 notas fictícias, máquina e concorrência registradas. Esse dataset ainda não foi gerado nem executado. Performance não remove policies/audit nem prefetch indiscriminado. Limiar é proposta de UX, não SLA garantido.

## Bloqueios concretos

EVAL-033 depende infraestrutura homologada, backup e plano clínico de contingência; EVAL-034 depende profissional da especialidade e ficha validada. Os demais dependem aplicativo a implementar. Antes de execução, nenhum deles tem executor ou relatório. Links e hash do pacote só demonstram integridade dos arquivos entregues.

Consulte [rubricas](rubrics.md), [rastreabilidade](../docs/traceability.md) e [limites](../docs/regulatory-and-clinical-boundaries.md).
