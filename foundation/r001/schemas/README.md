# Schemas e exemplos

Há um schema do modelo de fundação (`project-model.schema.json`, perfil Spec Foundry 1.0) e sete schemas propostos de domínio versão 0.1. Eles têm finalidades diferentes.

| Schema de domínio | Fixture correspondente |
|---|---|
| patient.schema.json | examples/patient.example.json |
| draft-command.schema.json | examples/draft-command.example.json |
| finalize-command.schema.json | examples/finalize-command.example.json |
| record-snapshot.schema.json | examples/record-snapshot.example.json |
| addendum-command.schema.json | examples/addendum-command.example.json |
| attachment.schema.json | examples/attachment.example.json |
| export-job.schema.json | examples/export-job.example.json |

Os arquivos são Draft 2020-12. `check_domain_contracts.py` usa jsonschema + FormatChecker; `common.py` valida apenas o subconjunto do modelo de fundação. Não afirmar que o validador portátil genérico implementa todos os recursos de JSON Schema.

Números, identidades e conteúdo das fixtures são fictícios. Datas de referência explícitas e estáticas permitem repetir testes sem depender do relógio; não são controles de produção. Relacionar IDs nas fixtures não verifica autorização real.

Entrada client e saída server têm formatos diferentes. Nunca reutilizar snapshot de saída como request que permita ao cliente escrever clinic_id, author_id, status ou scan_engine_version. O servidor futuro impõe policy e constraints além do schema.

`signature_status: not_implemented` torna explícito o limite da demo. Uma assinatura futura pede novo schema/revisão e evidência da solução homologada, não alterar o campo e declarar pronto.

Consulte [contratos humanos](../docs/data-contracts.md) e [operações propostas](../docs/application-commands.md). Esses schemas não completam todos os campos exigidos para cada profissão; não liberam prontuário real.
