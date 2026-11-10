# Comece aqui

1. Leia o README e [guia para iniciante](foundation/r001/docs/START-HERE.md).
2. Mostre [produto](foundation/r001/docs/specs/01-product-spec.md), [telas](foundation/r001/docs/ux-and-screen-contracts.md) e [perguntas](foundation/r001/docs/open-questions.md) a um profissional da área. Não use exemplos de pacientes reais nessa conversa.
3. Execute os checks após instalar requirements-dev: `python scripts/check_repository.py`.
4. Planeje TASK-001/002 do [backlog](foundation/r001/docs/specs/04-implementation-plan.md). Um app só começa depois que o recorte de desenvolvimento fictício foi acordado.
5. Trabalhe uma tarefa por vez. Não transforme verde da CI em autorização para pacientes reais.

## Prompt para Claude Code ou outra IA

```text
Leia README.md, AGENTS.md, CLAUDE.md e START-HERE.md.
Leia os anchors necessários em foundation/r001, sem alterar o snapshot.
Explique o MVP, as perguntas e os gates de uso real em português simples.
Planeje TASK-001/002, sem inventar respostas clínicas.
Depois da definição do recorte sintético, proponha uma única tarefa técnica pequena.
Antes de editar diga os arquivos e o plano; depois mostre diff, testes e limitações.
Não use dados reais, não faça deploy, não remova permissões/testes e não declare validação clínica.
```

O repositório ainda não contém aplicativo. Código futuro pode entrar em módulos do projeto em tarefa autorizada; não inserir em foundation/r001 nem regenerar a baseline para fazer um teste passar. Mudança material das definições pede r002.
