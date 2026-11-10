# Contratos de UX e telas — prontuário simples

> **Escopo da interface:** consultório ambulatorial brasileiro de adultos, uma clínica/instância e poucos usuários. Protótipo somente com dados sintéticos. Este documento define comportamento, conteúdo mínimo, permissões e avaliação; não exige um design visual novo.

## 1. Princípios não negociáveis

1. **Identidade clínica fixa.** Em toda tela de conteúdo clínico, exiba um banner fixo, não editável durante a leitura/edição, com: **nome completo**, **data de nascimento** e **número local do prontuário**. O banner deve permanecer visível em scroll ou ter equivalente persistente e acessível.
2. **Sem CPF obrigatório universal.** CPF pode ser um campo dependente de decisão futura, mas nenhum fluxo geral pode bloquear o cadastro apenas por ausência de CPF.
3. **Alergia é estado de registro, não inferência.** A interface nunca deve transformar ausência de informação em “sem alergia”. Use estados humanos e explícitos: `not_recorded` = não registrado; `none_reported` = paciente informou que não há alergia conhecida/relatada no contexto do registro; `known` = há alergia registrada, com detalhe conforme permitido. A ausência de uma marcação não é evidência de `none_reported`.
4. **Finalização não é assinatura digital.** O texto da interface deve dizer “Finalizar evolução” ou “Criar snapshot imutável”. Não use “assinar”, “assinatura digital” ou linguagem que prometa autenticidade jurídica não implementada.
5. **Permissão antes de conteúdo.** Recepção não vê conteúdo clínico. Admin não ganha conteúdo clínico por ser admin. Profissional só vê clínica quando houver vínculo clínico autorizado.
6. **Falha fechada.** Uma URL, busca, download, exportação ou mensagem de erro não pode vazar conteúdo para quem não tem autorização.
7. **Humano no circuito.** Não há diagnóstico, prescrição, sugestão clínica automática ou telemedicina no v1.
8. **Acessibilidade é requisito de função.** Contraste suficiente, foco visível, labels associados, navegação por teclado, ordem de foco coerente, mensagens textuais além de cor/ícone, alvos acionáveis compreensíveis e leitura compatível com tecnologia assistiva.
9. **Privacidade também vale para observabilidade.** Logs e mensagens técnicas usam IDs internos, tipo de ação, resultado e horário; não registram nome completo, data de nascimento junto com clínica, texto de evolução, alergia, anexo ou outro PHI em texto livre.

## 2. Papéis e matriz resumida

| Papel | Cadastro/agenda | Conteúdo clínico | Anexos clínicos | Exportação clínica |
| --- | --- | --- | --- | --- |
| **Recepção** | Sim, dentro do escopo permitido | **Não** | **Não** | **Não**, salvo uma permissão específica que não revele conteúdo durante o trabalho — decisão pendente |
| **Admin** | Conforme administração autorizada | **Não por ser admin** | **Não por ser admin** | **Não por ser admin** |
| **Profissional com vínculo clínico autorizado** | Conforme vínculo | **Sim, somente no escopo autorizado** | Conforme vínculo e política | Conforme permissão explícita e controle |
| **Usuário não autenticado** | Não | Não | Não | Não |

“Admin” pode administrar conta ou configuração, mas não deve receber uma porta dos fundos para prontuário. Uma tela negada deve revelar somente que a ação não é permitida, sem confirmar detalhes clínicos desnecessários.

## 3. Estados comuns a todas as telas

Toda tela deve ter uma representação pensada para os estados a seguir, conforme aplicável. O texto não pode depender apenas de cor.

| Estado | Contrato de comportamento |
| --- | --- |
| **Loading** | Informar que os dados estão carregando; preservar contexto e identidade já conhecida; impedir duplo envio; usar foco e leitor de tela de forma previsível. |
| **Empty** | Explicar o que está vazio e por quê; oferecer a próxima ação permitida; nunca preencher inferências clínicas. Ex.: “Nenhuma evolução registrada”, não “Paciente está bem”. |
| **Error** | Mensagem humana, ação de tentar novamente ou sair, código técnico apenas para suporte sem PHI; não apagar texto local não enviado. |
| **Permission denied** | Mensagem curta (“Você não tem permissão para acessar este conteúdo”), sem nome de doença, trecho clínico, nome de anexo ou existência desnecessária; registrar somente evento operacional sem PHI. |
| **Offline / conexão interrompida** | Informar que não é possível garantir leitura atual ou gravação; não prometer sincronização automática. Rascunho local, se algum dia existir, deve ser decisão explícita e protegido; no mínimo, bloquear envio sem confirmação de estado. |
| **Stale / conflito de versão** | Informar que outra alteração foi salva; não sobrescrever silenciosamente; mostrar opções seguras: recarregar versão atual, comparar versões autorizadas ou copiar texto para revisão manual. A decisão não deve apagar o trabalho atual. |
| **Success** | Confirmar exatamente o que ocorreu (“Rascunho salvo”, “Snapshot finalizado”, “Anexo enviado para quarentena”), nunca afirmar mais do que o sistema provou. |

## 4. As sete telas do MVP

As telas abaixo são um limite de prototipagem: não criar uma “tela geral” que misture papéis, agenda e conteúdo clínico. Estados secundários podem ser modais ou regiões da própria tela, mas não devem contornar autorização.

### T01 — Entrada e sessão

**Objetivo:** autenticar e encerrar sessão com segurança.

**Conteúdo mínimo:** identificador de login, senha, ponto de MFA quando homologado, botão entrar, link/ação de recuperação conforme política, encerrar sessão.

**Não mostrar:** pacientes, agenda ou qualquer conteúdo antes de autorização.

**Regras:** após autenticar, direcionar conforme papel e escopo; não revelar se um identificador pertence a uma conta; MFA é “a homologar”, então o protótipo deve marcar a decisão sem fingir que está implementada.

**Estados essenciais:** loading no envio; erro de autenticação genérico; permissão/conta bloqueada sem detalhes sensíveis; offline sem tentativa enganosa de login; success somente quando a sessão estiver estabelecida.

**Eval T01:** usuário não autenticado não abre as outras seis telas por URL direta; erro não enumera contas.

### T02 — Cadastro e busca de paciente (recepção)

**Objetivo:** criar ou localizar o registro administrativo mínimo de um adulto, com prevenção de duplicidade sem exigir CPF universal.

**Conteúdo mínimo:** nome completo, data de nascimento, número local do prontuário/registro e campos administrativos necessários que tenham sido decididos. Marcar dados sintéticos no protótipo.

**Não mostrar:** evolução, diagnóstico, alergia, adendo, anexo clínico, resumo clínico ou prévia de conteúdo.

**Regras:** CPF não é bloqueador universal; busca e confirmação devem evitar expor uma lista de pessoas a quem não precisa vê-la; duplicidade deve pedir revisão humana, não escolher automaticamente um paciente.

**Estados essenciais:** loading de busca; empty (“Nenhum registro encontrado”); erro de duplicidade ou serviço; permission denied para conteúdo clínico; offline bloqueia gravação ou deixa explícito que não foi salvo; stale exige recarga do cadastro.

**Eval T02:** recepção conclui cadastro sem CPF; ao abrir um paciente, permanece em área administrativa e não encontra campo/preview clínico.

### T03 — Agenda básica

**Objetivo:** visualizar e operar compromissos administrativos básicos.

**Conteúdo mínimo:** data/hora, paciente conforme autorização administrativa, profissional ou recurso conforme escopo, status do compromisso e ações permitidas.

**Não mostrar:** texto de evolução, alergias, anexos, diagnóstico ou resumo clínico. Um compromisso não é motivo para revelar prontuário.

**Regras:** conflitos de horário devem ser explícitos; alterações devem ter confirmação quando causarem impacto; conteúdo clínico não pode aparecer em tooltip, notificação, exportação de agenda ou log.

**Estados essenciais:** loading; empty (“Nenhum compromisso neste período”); erro ao salvar; permission denied para ações fora do papel; offline impede sincronização silenciosa; stale avisa quando a agenda mudou.

**Eval T03:** recepção consegue uma operação de agenda autorizada, mas nenhum texto clínico é renderizado no HTML, busca, resposta de erro ou exportação de agenda.

### T04 — Identidade e linha do tempo clínica (profissional autorizado)

**Objetivo:** oferecer contexto clínico autorizado sem misturar identidade nem permitir ação fora do vínculo.

**Cabeçalho fixo obrigatório:** **nome completo + data de nascimento + número local do prontuário**. Deve existir indicação clara de que o registro é do adulto selecionado e, no protótipo, de que os dados são sintéticos.

**Conteúdo mínimo:** linha do tempo de evoluções finalizadas e rascunhos que o profissional pode acessar; estado de alergia como `not_recorded`, `none_reported` ou `known`, com linguagem humana; adendos e anexos somente quando autorizados.

**Não mostrar:** “sem alergia” quando o estado for `not_recorded`; dados de outro paciente; conteúdo de outro vínculo; ações de edição de snapshot finalizado.

**Regras de identidade:** o banner permanece visível; troca de paciente exige confirmação/recarga inequívoca; se identidade não puder ser confirmada, não renderizar conteúdo clínico.

**Estados essenciais:** loading preservando identidade; empty distinguindo “nenhuma evolução registrada” de ausência de alergia; error sem PHI; permission denied genérico; offline informa que a linha do tempo pode estar desatualizada; stale exige tratar conflito antes de editar.

**Eval T04:** o banner contém os três identificadores; o estado `not_recorded` não vira “sem alergia”; profissional sem vínculo recebe negação sem conteúdo.

### T05 — Editor de evolução manual

**Objetivo:** permitir que profissional autorizado escreva e salve evolução manual como rascunho versionado.

**Conteúdo mínimo:** identidade fixa da T04, área de texto com label, indicação de autor/ator interno, estado do rascunho, versão, salvar rascunho e sair sem perder contexto. Campos estruturados adicionais só entram após decisão de especialidade/profissão.

**Não oferecer:** sugestão de diagnóstico, prescrição, autocomplete clínico de IA, chamada de telemedicina ou botão “assinar digitalmente”.

**Regras de versão:** salvar rascunho cria ou atualiza uma versão identificável; não apagar versões anteriores sem política aprovada; informar data/hora de salvamento e estado. A finalização é uma ação separada, com confirmação clara de irreversibilidade do snapshot.

**Estados essenciais:** loading ao abrir/salvar; empty no primeiro rascunho; erro preserva o texto que ainda não foi enviado; permission denied bloqueia conteúdo e ações; offline não confirma salvamento; stale impede sobrescrita silenciosa e oferece comparação/recarregamento.

**Eval T05:** duas gravações preservam versões; recusa de permissão não retorna o texto clínico; conflito stale não destrói o rascunho local; nenhum texto de UI diz que o snapshot é assinatura digital.

### T06 — Finalização, snapshot, adendo e anexos

**Objetivo:** separar claramente o que foi finalizado, o que é adendo posterior e o que é arquivo em quarentena ou disponível.

**Blocos obrigatórios:**

- ação “Finalizar evolução” / “Criar snapshot imutável” com confirmação;
- visualização somente leitura do snapshot, com versão e momento da finalização;
- ação “Adicionar adendo”, que cria registro novo e não altera snapshot;
- envio de anexo para **quarentena**, com nome técnico mínimo, estado do scan e mensagem de que ainda não está disponível;
- acesso a anexo somente após scan aprovado e autorização clínica;
- tratamento de falha, rejeição ou pendência do scan sem download.

**Não mostrar:** botão de editar snapshot; promessa de assinatura digital; anexo em área pública; conteúdo clínico para recepção/admin sem vínculo.

**Estados essenciais:** loading do snapshot/scan; empty (“Nenhum adendo” ou “Nenhum anexo aprovado”, sem inferência); erro de finalização/anexo; permission denied sem confirmar arquivo; offline não finaliza nem promete upload; stale impede finalizar uma versão que deixou de ser atual.

**Eval T06:** snapshot continua igual após adendo; upload fica em quarentena até scan aprovado; anexo rejeitado não baixa; conteúdo é invisível para papéis não autorizados.

### T07 — Exportação controlada e confirmação

**Objetivo:** permitir exportação apenas quando autorizada, com escopo deliberado, confirmação e registro operacional.

**Conteúdo mínimo:** tipo de solicitação e verificação de identidade/poderes do destinatário, escopo selecionável e visível, resumo do que será exportado, confirmação explícita, estado de processamento e resultado controlado. Titular não precisa apresentar justificativa clínica para obter sua própria cópia. Solicitações de terceiros exigem fundamento e análise apropriados, não checkbox genérico.

**Regras:** exigir permissão explícita; permitir cópia integral quando solicitada/autorizada, sem restringir indevidamente o direito do titular; mostrar ao usuário autorizado quais registros e anexos entrarão; respeitar quarentena e indicar os itens temporariamente indisponíveis; registrar evento técnico sem PHI no log; download deve ter proteção equivalente ao conteúdo.

**Não mostrar:** exportação para admin/recepção só porque possuem papel administrativo; conteúdo para quem não recebeu a autorização; mensagem de sucesso antes do artefato ser realmente gerado e protegido.

**Estados essenciais:** loading na preparação/geração; empty quando não há itens autorizados; erro sem revelar conteúdo; permission denied genérico; offline impede criação/entrega; stale revalida escopo antes de exportar.

**Eval T07:** usuário sem permissão não consegue inferir conteúdo pelo formulário; exportação respeita escopo e scan; confirmação identifica o que será incluído; log não tem PHI.

## 5. Contrato de conteúdo e linguagem

### Mensagens recomendadas

- “Rascunho salvo — versão 3.”
- “Evolução finalizada. Foi criado um snapshot imutável; ele não pode ser editado.”
- “Adendo criado. O snapshot original permanece inalterado.”
- “Anexo recebido e colocado em quarentena. Ele ficará disponível após a verificação e se você tiver permissão.”
- “Não foi possível confirmar o salvamento. Seu texto não foi descartado; verifique a conexão e tente novamente.”
- “Outra versão foi salva. Recarregue ou compare antes de continuar; nada foi sobrescrito.”
- “Você não tem permissão para acessar este conteúdo.”

### Mensagens proibidas ou perigosas

- “Assinado digitalmente” quando somente houve finalização/snapshot.
- “Sem alergia” quando não há registro explícito `none_reported`.
- “Paciente sem risco” ou qualquer conclusão clínica automática.
- “Admin pode ver tudo”.
- “Upload concluído” enquanto o arquivo está em quarentena.
- Mensagens ou logs que repitam o texto clínico, nome completo, data de nascimento, alergias ou conteúdo do anexo.

## 6. Critérios transversais de acessibilidade e privacidade

Para cada tela, a avaliação deve verificar:

- todo campo tem label textual associado e instrução compreensível;
- tudo que é acionável funciona por teclado, com foco visível e ordem coerente;
- erros ficam junto ao campo e em resumo anunciável, sem remover o texto digitado;
- contraste e estado não dependem apenas de cor;
- o banner de identidade é anunciado sem ambiguidade e não pode ser alterado acidentalmente;
- tabelas, listas e estados vazios têm cabeçalhos/nomes acessíveis;
- conteúdo clínico não aparece em título de notificação, URL, atributo de acessibilidade, console ou log técnico desnecessário;
- respostas de permissão negada têm o mesmo cuidado de privacidade que a tela protegida;
- timeout, logout e falha de rede informam o que foi ou não salvo;
- dados de demonstração estão identificados como sintéticos e não se parecem com uma pessoa real específica.

## 7. Matriz de avaliação resumida

| ID | Cenário | Resultado obrigatório | Tipo |
| --- | --- | --- | --- |
| `UX-PERM-01` | Recepção abre paciente | Vê cadastro/agenda autorizados; não vê conteúdo clínico em nenhuma tela ou resposta | Mock/aplicação |
| `UX-PERM-02` | Admin tenta linha do tempo clínica | Negação fechada; papel admin não concede acesso | Mock/aplicação |
| `UX-PERM-03` | Profissional sem vínculo tenta evolução | Negação fechada; sem confirmação ou vazamento de conteúdo | Mock/aplicação |
| `UX-ID-01` | Profissional autorizado abre registro | Banner fixo tem nome completo, data de nascimento e número local | Mock/aplicação |
| `UX-ID-02` | Cadastro sem CPF | Fluxo não bloqueia por CPF ausente | Mock/aplicação |
| `UX-ALLERGY-01` | Alergia não registrada | Exibe `not_recorded` em linguagem humana; não diz “sem alergia” | Mock/aplicação |
| `UX-VERSION-01` | Salvar duas vezes | Versões permanecem recuperáveis conforme política; atual não apaga anterior | Aplicação |
| `UX-FINAL-01` | Finalizar evolução | Snapshot imutável; nenhuma linguagem de assinatura digital | Mock/aplicação |
| `UX-ADD-01` | Criar adendo | Adendo separado; snapshot original inalterado | Mock/aplicação |
| `UX-FILE-01` | Enviar anexo | Quarentena/scan antes de acesso; rejeitado não baixa | Aplicação |
| `UX-EXPORT-01` | Exportar escopo autorizado | Confirmação mostra escopo; somente itens permitidos e aprovados entram | Aplicação |
| `UX-STATE-01` | Interromper rede em cada fluxo | Loading/erro/offline não inventam sucesso nem descartam texto | Mock |
| `UX-CONFLICT-01` | Salvar versão stale | Usuário é avisado e não há sobrescrita silenciosa | Aplicação |
| `UX-A11Y-01` | Navegar sem mouse | Labels, foco, teclado e mensagens funcionam | Mock/aplicação |
| `UX-LOG-01` | Inspecionar eventos técnicos | Logs não contêm PHI | Aplicação/revisão de log |

Um caso com decisão de política ainda aberta deve ser marcado como **bloqueado**, com a pergunta registrada. Não preencher o buraco com uma suposição de UX.

## 8. Fora deste contrato

Não fazem parte destas sete telas nem devem ser adicionados por conveniência:

- fluxos para menores, guardiões ou consentimento pediátrico;
- diagnóstico, prescrição, recomendação clínica por IA ou telemedicina;
- financeiro, convênios, TISS, FHIR, SUS ou integrações externas;
- assinatura digital ou afirmação de validade jurídica;
- seleção de especialidade/profissão não decidida;
- design visual ou marca nova;
- uso de dados reais para prototipagem.

Antes de uso real, este contrato precisa passar por responsável clínico, revisão especializada de assinatura/conselho/LGPD, engenharia de segurança e operação de backup/restore em homologação. Um protótipo aprovado nos critérios acima ainda não é autorização de produção.
