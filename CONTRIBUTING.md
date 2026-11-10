# Contribuindo

Obrigado por contribuir com a fundação pública do **Prontuário simples**. Este repositório começa como uma especificação em discovery, para uma pessoa iniciante aprender a construir com Claude ou outra IA como apoio de programação. A fundação não é um aplicativo, prontuário certificado, autorização para atender pacientes ou aprovação clínica.

## Antes de começar

Leia, nesta ordem:

1. [`README.md`](README.md), [`AGENTS.md`](AGENTS.md), [`CLAUDE.md`](CLAUDE.md) e [`START-HERE.md`](START-HERE.md) na raiz;
2. [`foundation/r001/README.md`](foundation/r001/README.md) e [`foundation/r001/AGENTS.md`](foundation/r001/AGENTS.md);
3. o plano de implementação em [`foundation/r001/docs/specs/04-implementation-plan.md`](foundation/r001/docs/specs/04-implementation-plan.md) e as instruções para a IA em [`foundation/r001/docs/specs/05-agent-configuration.md`](foundation/r001/docs/specs/05-agent-configuration.md);
4. [`foundation/r001/evals/eval-spec.md`](foundation/r001/evals/eval-spec.md), se a tarefa envolver avaliação.

A `foundation/r001` é um snapshot imutável, verificado por [`foundation/r001/manifest.json`](foundation/r001/manifest.json). Não edite, mova ou exclua arquivos nela. Uma mudança material de requisitos, profissão, clínica, assinatura, fornecedor, storage ou escopo deve ser proposta como **r002**, com diff de impacto, contratos, tarefas, riscos e avaliações atualizados. Não reaproveite aprovação ou relatório de uma revisão em outra.

## Uma tarefa por vez

Não peça “faça o sistema inteiro”. Para cada tarefa:

1. Escolha um único card pequeno e registre objetivo, arquivos e limites.
2. Peça à IA um plano antes de editar; não aceite respostas inventadas para perguntas clínicas, de campos, assinatura, privacidade ou operação.
3. Trabalhe somente com dados fictícios. Nunca coloque pacientes, exames, documentos, e-mails reais, tokens, chaves ou dados de saúde em prompts, issues, commits, logs, testes ou screenshots.
4. Faça o menor diff possível. Não crie app, infraestrutura ou integração como consequência automática de uma tarefa documental.
5. Execute a verificação adequada e mostre o diff, os testes e as limitações. Se algo não puder ser executado, marque como `blocked` ou `not_run`; não remova o teste nem transforme ausência de evidência em aprovação.
6. Pare ao terminar a tarefa e peça revisão humana quando houver decisão de domínio, segurança ou operação.

Um pedido inicial seguro para o Claude é:

```text
Leia README.md, AGENTS.md, CLAUDE.md, START-HERE.md e os arquivos da tarefa.
Explique o escopo e os bloqueios sem inventar respostas.
Trabalhe em uma única tarefa, somente com dados fictícios.
Antes de editar, mostre o plano e os arquivos que serão alterados.
Depois, mostre o diff, execute os testes disponíveis e liste as limitações.
Não altere foundation/r001, não crie app e não faça deploy.
```

## Verificação local

Use Python 3.11+ em um ambiente virtual. Instale o arquivo da raiz (`jsonschema[format-nongpl]==4.26.0`), não apenas o jsonschema básico: o extra fornece a validação RFC3339 usada nos testes de data/hora com fuso. Ele não altera os contratos nem a baseline r001.

```bash
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows PowerShell, em vez do comando acima:
# .venv\Scripts\Activate.ps1

python -m pip install -r requirements-dev.txt
python scripts/check_repository.py
```

A verificação é offline e não precisa de segredos, serviços externos, banco remoto ou dados clínicos. Ela confere o repositório e a fundação; não executa aplicativo, autenticação, autorização HTTP, assinatura, scanner, backup remoto, atendimento ou validação profissional. A CI deve conservar esse caráter offline e sem segredos.

O estado r001 registra 20 requisitos, 15 cards e 34 casos-alvo. Os 34 casos do sistema-alvo ainda não foram executados; os testes offline da fundação registrados na entrega somam 23 testes aprovados. Isso não transforma nenhum caso do aplicativo em `passed` nem autoriza uso real.

## Dados, saúde e licença

A próxima implementação, quando autorizada, deve ser **sintética**: fixtures fictícias, ambiente de teste e comportamento explicitamente separado da operação clínica. Uso real exige decisões e revisões humanas apropriadas, incluindo profissão, campos, permissões, preservação/assinatura, privacidade, backup/restauração, segurança e suporte. “A tela funciona” não é um gate de uso real.

A licença MIT permite reutilizar o código e a documentação nos termos da licença; não certifica segurança, qualidade clínica, conformidade ou adequação a qualquer serviço, e não autoriza uso irresponsável de dados de saúde. Não adicione uma política legal, uma recomendação de produção ou uma aprovação que não tenha sido fornecida e registrada.

## Pull requests e issues

Descreva uma mudança por pull request ou issue. Inclua:

- tarefa ou motivo e escopo que a mudança atende;
- arquivos alterados e diff relevante;
- comando(s) executado(s) e resultado;
- dados/fixtures usados, sempre fictícios;
- limitações, casos `blocked`/`not_run` e revisão humana ainda necessária;
- se houver mudança material, a proposta de r002 e seu registro de impacto.

Não publique conteúdo de pacientes ou outros dados pessoais para demonstrar um bug. Uma issue deve ser reproduzível com dados sintéticos e não deve conter e-mails reais, credenciais ou segredos. Código e validação do aplicativo são trabalho futuro; não apresente contratos, schemas, mocks ou checks offline como certificação.
