# Contexto do Claude

A meta é ajudar uma pessoa não técnica a construir um prontuário manual simples com IA como apoio de programação, não dentro do atendimento clínico. Não há app/banco/infra no pacote. A fundação está em discovery, com gates de uso real abertos.

Leia [AGENTS.md](AGENTS.md) e [guia de início](docs/START-HERE.md). O modelo canônico é model/project-model.json; cases.json deve concordar com eval_cases. Requisitos/decisões são proposed até resposta humana da revisão correta. O manual de código é [anchor 05](docs/specs/05-agent-configuration.md).

Proposta de stack: Django 5.2 LTS com patch suportado, templates, PostgreSQL, auth/sessions e django-allauth MFA a homologar; storage privado. Não substituir por SPA ou microserviços porque consegue gerar boilerplate. Valide recorte primeiro.

Primeiras tasks: TASK-001/002 discovery; TASK-003/004 contas e policies em demo após concordância com recorte sintético. Use fixtures fictícias; nenhum paciente real em prompts. Antes de sugerir produção, verificar TASK-014/015 e todas as perguntas pertinentes.

Comando de qualidade do pacote: `python scripts/check_foundation.py`. Os testes são de contrato/fundação; versões, HTTP, policy de acesso, scanner, signature e restore da aplicação ainda serão implementados e avaliados. Apresente resultados e limitações em separado.
