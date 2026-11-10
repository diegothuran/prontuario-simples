# Desenvolvimento

Este guia descreve como evoluir a fundação do **Prontuário simples** com segurança. O repositório público começa em `r001`, em estado **discovery**. Há especificações, contratos, exemplos e validadores offline; não há aplicativo, banco, autenticação, storage, assinatura ou infraestrutura prontos.

## Escopo atual

A hipótese inicial é um consultório ambulatorial adulto, uma clínica e poucos usuários. O fluxo proposto é: cadastro/localização do paciente → agenda → atendimento manual → rascunho → snapshot fechado → histórico/adendo → cópia autorizada. Profissão, especialidade, clínica, campos da ficha, responsáveis, assinatura e operação ainda precisam de resposta humana.

Não estão aprovados: campos clínicos, assinatura, uso de pacientes reais, IA clínica/transcrição, diagnóstico, dose, receita, atestado, telemedicina, hospital, financeiro, convênios, integrações ou sincronização offline. Os exemplos e schemas são contratos propostos com dados fictícios, não prontuários nem “gold” clínico.

O snapshot r001 registra 20 requisitos, 15 cards e 34 casos-alvo não executados. Os 23 testes offline já aprovados verificam apenas a camada de pacote/contratos. Eles não demonstram que um aplicativo funciona, que uma permissão é segura, que a ficha é adequada ou que há conformidade.

## Fluxo para iniciante

Trabalhe uma tarefa pequena por vez, usando Claude ou outra IA apenas como apoio de programação:

1. Leia a tarefa, as perguntas abertas e os limites em `foundation/r001`.
2. Escreva o objetivo e a definição de pronto em linguagem simples.
3. Peça um plano com os arquivos a alterar; aguarde a revisão do plano.
4. Use exclusivamente fixtures e dados fictícios.
5. Faça um diff pequeno.
6. Execute a verificação adequada e registre comando, resultado e ambiente.
7. Explique o que o teste não cobre e pare para revisão antes da próxima tarefa.

Prompt curto:

```text
Leia a documentação da tarefa e explique o que está decidido e o que está bloqueado.
Proponha uma única mudança pequena, usando apenas dados fictícios.
Antes de editar, liste os arquivos e o plano.
Depois, mostre o diff, os testes e as limitações.
Não altere foundation/r001, não invente aprovação clínica e não crie o sistema inteiro.
```

## Verificação local

Na raiz do repositório:

```bash
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows PowerShell, em vez do comando acima:
# .venv\Scripts\Activate.ps1

python -m pip install -r requirements-dev.txt
python scripts/check_repository.py
```

A dependência de desenvolvimento da raiz é `jsonschema[format-nongpl]==4.26.0`. O extra é necessário para rejeitar timestamps RFC3339 sem fuso: jsonschema básico pode deixar a checagem de formato inativa. A primeira CI expôs essa ausência, reproduzida em venv mínimo; a correção instala o suporte, sem remover o teste ou alterar foundation/r001. Use requirements-dev.txt da raiz, que complementa o ambiente histórico da baseline.

O comando de verificação é portátil, offline e não usa segredos. Ele valida a organização e os contratos da entrega; não substitui testes de aplicação. Instalar dependências e baixar as Actions exige internet; os checks não consultam APIs, bancos remotos, pacientes ou serviços de produção.

Ao relatar uma execução, separe as camadas:

- **Pacote/contratos:** arquivos, links, schemas, exemplos, invariantes e integridade do snapshot.
- **Aplicação futura:** navegador, sessões, MFA, permissões por objeto, concorrência PostgreSQL, storage privado, scanner, exportação, auditoria e restore.
- **Revisão humana/operação:** profissão, ficha, assinatura/preservação, privacidade, contingência, suporte e decisão de release.

Se uma camada não foi executada, registre `blocked` ou `not_run`. Não mude casos-alvo para `passed` por causa do check offline.

## Próxima implementação: sempre sintética primeiro

Depois de TASK-001 e TASK-002 definirem o recorte e a ficha de forma humana, uma tarefa técnica autorizada pode criar código em ambiente sintético. O código futuro deve preservar permissões no servidor, identidade e autoria derivadas de contexto confiável, histórico sem sobrescrever finalizados e ausência de PHI em logs/prompts. A stack proposta no snapshot é Django LTS com templates e PostgreSQL; ela é uma proposta, não uma ordem irreversível.

A implementação sintética não é uso real. Antes de qualquer paciente ou operação, ainda seriam necessários, no mínimo, revisão profissional e técnica, controles de acesso, preservação/assinatura apropriadas, privacidade, backup restaurado, plano de incidente e decisão documentada de release. Código e validação do app são trabalho futuro.

## Mudanças e imutabilidade

Não edite, regenere, mova ou exclua arquivos de `foundation/r001`. Seu [`manifest.json`](../foundation/r001/manifest.json) verifica o snapshot por hashes; hash não é assinatura, identidade humana ou aprovação clínica.

Uma mudança material — inclusive profissão, população, clínica, campos, assinatura, fornecedor/storage, IA ou escopo — exige `r002`, diff de impacto e atualização coerente de requisitos, contratos, tarefas, riscos e evals. Aprovações e relatórios pertencem à revisão em que foram produzidos; não devem ser copiados para um release novo.

Para cada alteração permitida na raiz, registre:

```text
Tarefa:
Objetivo:
Arquivos alterados:
Diff resumido:
Comando(s) e resultado:
Dados fictícios usados:
Limitações / blocked / not_run:
Revisão humana ainda necessária:
```

Não inclua e-mails reais, pacientes, exames, documentos, tokens, chaves ou dados de saúde. A licença MIT não certifica o projeto nem permite uso irresponsável de dados de saúde; também não é motivo para inventar política legal ou recomendação de produção.
