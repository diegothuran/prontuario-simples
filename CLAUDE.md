# Contexto do Claude

Leia [AGENTS.md](AGENTS.md), [START-HERE.md](START-HERE.md) e [guia da fundação](foundation/r001/docs/START-HERE.md). Primeiro objetivo: entender e executar uma pequena tarefa de discovery/implementação sintética autorizada, não gerar o prontuário inteiro.

A baseline canônica r001 está em foundation/r001/model/project-model.json; o snapshot completo está protegido por manifest. Não modificá-lo. Sem aprovação clínica/assinatura/hospedagem/operação registrada, produto continua em discovery. Código de app e testes de runtime são trabalho futuro fora dessa pasta.

Stack proposta: Django LTS/templates/PostgreSQL, auth/MFA de biblioteca a homologar, storage privado. Não inferir profissional/especialidade pelo nome dos modelos. Só fixtures fictícias, sem IA sobre dados clínicos.

Check da raiz: `python scripts/check_repository.py`. Ele roda a verificação exportada e os testes offline da r001. Os 34 casos-alvo não são executados por isso. Para contribuições, leia [CONTRIBUTING.md](CONTRIBUTING.md). Mudar domínio/assinatura/IA ou política pede r002 com riscos, tasks e evals revisados.
