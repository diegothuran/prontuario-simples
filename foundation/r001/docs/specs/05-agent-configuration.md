# 05 — Instruções para a IA implementadora

Você ajuda um iniciante a construir um prontuário simples; não é profissional clínico, encarregado, auditor ou certificador. Este repositório começa como fundação r001 em discovery. Nenhum resultado local de contrato autoriza pacientes reais.

## Ordem

Leia README, docs/START-HERE.md, specs 01/02/03/04, domain-model, regulatory-and-clinical-boundaries, data-contracts, evals/eval-spec e open-questions. Faça uma tarefa pequena por ciclo, mostre plano/diff/comando de teste e explique em português simples. Não substitua lacunas por suposições silenciosas.

## Limites

Não usar dados, exames, fotos ou documentos reais em prompts, exemplos, testes, screenshots, issues ou logs. Não enviar prontuário a uma LLM. Não produzir diagnóstico, dose, classificação de urgência ou receita. Não ampliar escopo para microserviços, hospital ou IA porque um concorrente anuncia isso.

Não chamar snapshot de assinado; `signature_status` continua `not_implemented` na demo. Não ativar produção por troca de flag. Não inventar certificado, selo, base legal ou cadastro profissional verificado. Não apagar notas finalizadas nem remover testes que exponham falha.

## Código esperado depois

Usar a stack proposta apenas após a decisão de implementação ser registrada. Sessões/CSRF, ORM parametrizado, auth/MFA de biblioteca e checks de permissão por objeto, no servidor. Autor, clínica, papel e timestamps derivam do contexto confiável; rejeitar campos indevidos. Banco PostgreSQL nos testes de concorrência, não SQLite como substituto que esconda diferenças transacionais.

Separar DTOs de comando e snapshots. Importar fixtures em ambiente fictício não equivale a migração validada. Em migrations, nunca reconstruir histórico com data/autor fabricado. Escapar texto livre. Não tornar bucket público para resolver download. Não criar credencial de admin para todo mundo.

## Checks e entrega

Executar `python scripts/check_foundation.py` valida esta fundação, não o app. No aplicativo futuro, reportar unitários, integração PostgreSQL, navegador/fluxo, segurança e restore separados; se ferramenta/serviço faltar, marcar blocked, não passed. Atualizar evals/cases.json e modelo juntos. Toda execução de target_system precisa evidência do release, ambiente, fixture, executor, resultado e limitações.

Mudanças materiais criam r002 e registro de impacto; não declarar accepted/approved_baseline sem aprovação humana da revisão/escopo. Nunca fazer deploy, merge, cadastro de pacientes ou exclusões por inferência. O usuário autoriza essas ações separadamente.

## Prompt curto para começar

“Leia a fundação e as perguntas abertas. Explique o MVP e os bloqueios em linguagem simples. Não implemente tudo. Planeje primeiro TASK-001 e TASK-002, usando apenas dados fictícios. Para a primeira tarefa técnica aprovada, apresente os arquivos necessários, faça uma mudança pequena e teste sem afirmar prontidão clínica.”
