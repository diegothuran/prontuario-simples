# Comece aqui — guia para o amigo

Você recebeu o mapa para construir um prontuário simples, não um aplicativo pronto. **Pode começar a aprender e programar com dados fictícios. Não use pacientes reais antes da revisão profissional e técnica.** Ser iniciante não impede criar um protótipo; apenas exige não pular controles que você ainda não consegue revisar sozinho.

## 1. Entenda a primeira versão

Hipótese: consultório ambulatorial de adultos, uma clínica e poucos usuários. Profissão e especialidade ainda precisam ser definidas.

Fluxo: cadastrar/localizar paciente → agenda → abrir consulta → profissional escrever → salvar rascunho → finalizar registro fechado → consultar histórico/adendos → anexar/fornecer cópia autorizada.

Não começar por hospital, IA diagnóstica/transcrição, receitas/atestados, telemedicina, convênios, financeiro, aplicativo de celular ou integrações. A lista de funções dos concorrentes é maior que o nosso primeiro problema.

## 2. O que perguntar ao profissional

Use as [perguntas abertas](open-questions.md). Primeiro escolha profissão/especialidade, veja uma consulta narrada do começo ao fim sem dados de paciente, confirme quem acessa o quê e os campos usados. Nenhuma resposta pode ser inventada pela IA.

Antes de uso real, precisa responsável clínico da profissão correta, revisão de segurança por engenheiro experiente, privacidade/assinatura/preservação, backup restaurado, suporte e aprovação do release. Não chamar de POC para dispensar esse trabalho.

## 3. Regras que você deve saber explicar

- Recepção cuida de cadastro/agenda; não lê conteúdo clínico. Admin não vê tudo por ser admin. Profissional precisa vínculo assistencial autorizado com o paciente.
- Nome, data de nascimento e número local ajudam a confirmar quem está na tela. Homônimos não são automaticamente a mesma pessoa. CPF não é universalmente obrigatório no cadastro mínimo fictício.
- Salvar é confirmar gravação no servidor; se a internet caiu, não pode dizer Salvo sem comprovação.
- Finalizar cria registro fechado. Correção depois vira adendo e preserva o original.
- Finalização, nome digitado e hash não equivalem a assinatura digital legalmente suficiente. Na demo, assinatura está não implementada.
- Anexo privado fica em quarentena até inspeção; arquivo enviado não é arquivo já liberado.
- Não registrado não significa Sem alergia ou Exame normal.
- Dados clínicos não vão para prompts, prints públicos, Git, logs ou analytics.

## 4. Escolha técnica recomendada

Django LTS + páginas server-side + PostgreSQL. Login/sessão de biblioteca, MFA a homologar, storage privado. Um monólito é um aplicativo único organizado em módulos, não código bagunçado. Não há SPA/microserviços neste recorte. A escolha é proposta para reduzir trabalho, não obrigação irreversível.

Não há código de aplicativo neste pacote. Depois que o recorte de desenvolvimento fictício for acordado, uma tarefa autorizada pode criar a estrutura Django e seus testes. Isso não aprova dados reais. Se perguntar algo que depende da profissão ou assinatura, pause essa parte e registre a dúvida; continue apenas o trabalho independente seguro.

## 5. Use IA uma tarefa por vez

Abra a pasta do projeto no seu ambiente/Claude Code e peça:

```text
Leia README.md, AGENTS.md, docs/START-HERE.md e os arquivos da tarefa.
Explique o MVP e os bloqueios sem inventar respostas.
Planeje TASK-001 e TASK-002 primeiro, só com dados fictícios.
Depois de definido o recorte sintético, trabalhe uma única tarefa técnica autorizada.
Antes de editar, diga o plano e os arquivos; depois mostre o diff e os testes.
Não faça deploy, não conecte dados reais e não apresente teste de contrato como validação clínica.
```

Evite “faça o sistema inteiro”. Peça mudança pequena, confira o que mudou, execute o teste e só então avance. Se um teste falhar, não permita que a IA apague o teste ou desligue a permissão só para ficar verde. Peça ajuda técnica quando não conseguir revisar o efeito.

## 6. Verifique o pacote recebido

Python 3.11+ instalado. Na pasta extraída:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python scripts/check_foundation.py
```

Se o terminal diz que não encontra Python/pip, resolva a instalação local antes de pedir para a IA reescrever o projeto. Esse comando não liga prontuário nem faz deploy; só verifica os arquivos da fundação e contratos offline. Dados, credenciais e custos cloud não são necessários para ele.

## 7. Diferencie verificações

| Tipo | O que demonstra | O que não demonstra |
|---|---|---|
| Pacote/contrato | Arquivos, links, estrutura e invariantes fictícias conferem | Aplicação funcionando, segurança clínica, conformidade |
| Mock de UI | Estados/mensagens/fluxo da simulação | Banco, scanner, login, integração ou operação reais |
| Aplicação de teste | Comportamento observado do release no ambiente descrito | Aprovação profissional ou segurança em todo cenário |
| Revisão especializada | Adequação ao contexto e decisão documentada da revisão | Garantia de ausência universal de falhas |

“Passou” só é útil com camada, versão, evidência e limites. Os casos do produto em [evals](../evals/eval-spec.md) ainda estão não executados/bloqueados; eles dizem o que você deverá provar depois.

## 8. Seu primeiro checkpoint

Você consegue explicar: quem acessa o quê; paciente correto; o que acontece se cair a internet; diferença entre rascunho/finalizado/assinado; como corrigir sem apagar; onde os anexos são guardados; como recuperar tudo; quem valida antes do primeiro paciente real?

Se ainda não, converse com o parceiro usando [telas e estados](ux-and-screen-contracts.md) antes de construir mais telas. O objetivo é ser capaz de revisar as decisões, não apenas aceitar código que aparece bonito.

## Glossário

Spec = descrição do que construir. Eval spec = como verificar. Snapshot = versão fechada. Adendo = complemento atribuído sem apagar original. MFA = segundo fator no login. Policy = regra de acesso. 409/stale = outra gravação mudou a versão. PHI = abreviação usada nos documentos para informação de saúde identificável, não invocação automática da lei americana HIPAA. RPO = quanto dado pode ser perdido numa falha; RTO = tempo para recuperar operação. Restore = restaurar backup e comprovar que os dados/arquivos voltaram juntos.
