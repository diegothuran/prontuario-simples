# Pesquisa: iClinic como prontuário eletrônico para consultório brasileiro

**Data de referência:** 10/11/2026  
**Escopo:** somente Afya iClinic/iClinic e páginas oficiais. Não houve login, criação de conta nem ações em dados.

## Leitura rápida

O iClinic apresenta um prontuário em nuvem que combina cadastro, atendimento, campos configuráveis, documentos, prescrições e histórico com agenda e outros módulos. Para um prontuário simples de iniciante, a parte mais aproveitável é o fluxo linear **cadastrar paciente → abrir atendimento → preencher campos → salvar → encerrar → consultar histórico**, com permissões básicas, anexos e registro posterior sem sobrescrever o original. Agenda, prescrição digital, financeiro, teleconsulta, mensagens e IA aparecem como módulos ou camadas adicionais, não como requisitos do núcleo.

A maior cautela é separar capacidade descrita de validação independente: as páginas são material comercial e de suporte do próprio fornecedor. A existência da função no site não comprova desempenho clínico, disponibilidade no plano desejado, qualidade da transcrição, certificação ou conformidade jurídica auditada.

## Fluxo observado

### 1. Cadastro

O suporte oficial documenta dois caminhos: a recepção acessa **Pacientes → Novo Paciente**; o profissional de saúde acessa **Prontuários → Novo Paciente**. O cadastro exige, no mínimo, nome, data de nascimento, sexo e pelo menos um telefone; depois os demais dados podem ser preenchidos e salvos. O resultado é o mesmo, mudando apenas o perfil de acesso [1].

**Capacidade a aproveitar:** cadastro simples, com entrada própria para recepção e profissional, validação de campos mínimos e separação de papéis.

**Para um iniciante:** começar com identificação, contatos e poucos dados administrativos essenciais. Não replicar a amplitude de cadastros, convênios ou campos de especialidade sem confirmação do uso real.

### 2. Atendimento, anamnese e evolução

O atendimento pode começar a partir da **Agenda** ou da seção de **Prontuários**. Ao abrir o paciente, o profissional seleciona **Iniciar atendimento**; o sistema inicia um cronômetro e libera as abas do prontuário. O suporte afirma que os campos podem ser preenchidos sem obrigatoriedade e que o salvamento ocorre pelo botão **Salvar**. Ao final, usa-se **Encerrar consulta** [2].

A página do produto descreve um prontuário personalizável por especialidade, com campos de texto, numérico, múltipla escolha e data; também menciona busca em tabelas, cálculos e seções organizadas por tipo de atendimento [3]. Ela apresenta o PEP como centralizador de histórico, exames, documentos e prescrições, com um fluxo comercial “antes/durante/depois” [3].

O material consultado não expõe uma tela ou uma taxonomia própria chamada “anamnese” e “evolução” com campos mínimos universais. A anamnese é inferida apenas como parte configurável do prontuário e como exemplo de conteúdo gerado pela IA. Portanto, para um produto iniciante, tratar anamnese e evolução como seções configuráveis e confirmar com o clínico seus nomes, ordem, obrigatoriedades e possibilidade de rascunho.

**Ponto importante de integridade:** o tutorial de suporte diz que, depois de encerrado o atendimento, as informações originais não podem ser editadas. Outra página explica que é possível inserir informação ou imagem adicional, ou retificar algo, sem alterar o registro original; a nova entrada fica abaixo da consulta com data e horário [2] [4]. Esse padrão de “registro original + adendo datado” é uma capacidade valiosa para aproveitar, mas deve ser validado no produto-alvo quanto a permissões e auditoria.

### 3. Histórico, anexos e documentos

O iClinic anuncia histórico, exames, documentos e prescrições organizados no prontuário. A página de recursos lista abas de **Anexos**, **Documentos** e **Histórico**, além de histórico de valores em tabela ou gráfico e comparação de imagens [3]. O suporte confirma que um adendo pós-consulta pode incluir texto ou imagens [4].

**Capacidade a aproveitar:** uma linha do tempo por paciente, consulta encerrada preservada, adendo posterior datado, anexos e documentos separados do texto clínico. Para uma primeira versão, limitar anexos a formatos e tamanho definidos, registrar data, autor e relação com o atendimento, e tornar explícito se o arquivo é apenas visualização ou também pode ser baixado/compartilhado.

### 4. Acesso e compartilhamento

O fornecedor afirma que o prontuário fica em nuvem e pode ser acessado em computador, tablet e celular, incluindo aplicativos Android e iPhone; também afirma que o registro é o mesmo entre dispositivos [3]. O suporte, por sua vez, informa que o acesso aos prontuários é liberado somente ao profissional de saúde e que o cadastro pode ser feito por recepção ou profissional conforme o perfil [2] [1]. A página comercial anuncia permissões por usuário e compartilhamento do prontuário com profissional específico ou toda a equipe [3].

**Capacidade a aproveitar:** papéis separados, acesso por usuário e compartilhamento explícito por paciente/equipe. Para iniciante, não transformar “acesso em qualquer dispositivo” em atalho para permissões amplas: definir o que recepção pode ver, o que pode editar e se pode anexar ou apenas cadastrar/agendar.

## Funcionalidades opcionais e integrações anunciadas

- **Agenda:** agenda integrada ao prontuário, agendamento online, confirmações e lembretes por e-mail, SMS ou WhatsApp aparecem nas páginas comerciais e nos planos [3] [5]. Para o núcleo simples, basta um agendamento associado ao paciente e ao atendimento; automações de comunicação podem ficar para depois.
- **Prescrição e documentos:** o iClinic anuncia prescrição digital, emissão de documentos e solicitações de exames, com assinatura digital e envio ao paciente [3] [5]. Aproveitar como módulo posterior, com revisão obrigatória do profissional e templates controlados; não assumir que assinatura está incluída em todos os planos, pois o material de preços também lista assinatura como adicional [3].
- **Financeiro:** os planos e a página institucional anunciam fluxo de caixa, dashboard, receitas e despesas, repasse por profissional, TISS, lançamento financeiro pela agenda/prontuário, estoque, pagamentos e recebíveis [3] [5]. É uma expansão de gestão, não requisito do prontuário inicial.
- **IA:** a página específica descreve ativação por clique, transcrição em tempo real, identificação de termos técnicos e geração de rascunho estruturado; o profissional revisa e salva. Ela também afirma que o áudio é apagado após o processamento e que a transcrição exige conexão ativa [6]. O produto principal informa IA incluída nos planos, enquanto a página de preços mais antiga lista “iClinic Assist” como complemento; essa diferença de posicionamento precisa ser confirmada comercialmente [3] [5] [6]. Para iniciante, IA deve ser opcional, nunca substituir revisão, e o fluxo precisa deixar claro consentimento, status de rascunho e autoria.
- **Integrações:** são anunciadas integrações com WhatsApp, assinatura ICP-Brasil, padrão TISS, pagamento integrado, Agendar Consulta, AWS e Glic [3]. Isso demonstra possibilidades, mas não detalha APIs, escopo de sincronização, tratamento de falhas ou disponibilidade por plano; não projetar essas integrações sem confirmação.
- **Teleconsulta e comunicação:** teleconsulta integrada, chat, campanhas de e-mail, pesquisa de satisfação e visibilidade/agendamento online são anunciados como módulos ou diferenças de plano [3] [5]. Excluir do primeiro corte se o objetivo for apenas prontuário de consultório.

## Segurança: declaração comercial versus verificação

**Declarações do fornecedor, não auditoria independente:** as páginas afirmam “conformidade com a LGPD”, base legal definida, encarregado, criptografia de 256 bits, hospedagem AWS, permissões por usuário, compartilhamento controlado e assinatura digital com validade jurídica [3]. A página de IA acrescenta que o áudio é processado em tempo real, deletado em seguida e não compartilhado com terceiros [6]. A página de preços também declara backup diário, criptografia e segurança “nível bancário” [5].

**O que foi efetivamente verificado nesta pesquisa:** apenas que essas afirmações estão publicadas em páginas oficiais e que o suporte descreve bloqueio de edição do registro encerrado, adendo datado e acesso do prontuário restrito ao profissional [1] [2] [4]. Não foram testados login, permissões, exportação, logs, criptografia, backup, exclusão de áudio, assinatura, segregação de dados ou qualquer controle técnico. Não há, neste levantamento, validação de certificação ou relatório de auditoria. Não presumir conformidade, certificação ou validade jurídica para o produto a ser construído apenas com base nessas declarações.

## O que aproveitar e o que excluir para iniciante

**Aproveitar no núcleo:** cadastro com papéis; paciente como entidade central; atendimento iniciado a partir do paciente ou agenda; campos configuráveis de anamnese/evolução; salvar e encerrar; histórico cronológico; anexos; adendo posterior sem sobrescrever o original; autor, data e hora; permissões mínimas; exportação e recuperação a serem confirmadas com o clínico.

**Deixar fora do primeiro corte:** IA e transcrição; teleconsulta; WhatsApp e campanhas; TISS; financeiro, repasse, estoque, pagamentos e recebíveis; Glic; assinatura digital; calculadoras específicas, odontograma, vacinas e recursos de especialidade; migração automatizada; dashboards e relatórios extensos. São capacidades anunciadas pelo iClinic, mas aumentam risco, escopo e necessidade de validação.

## Perguntas para o clínico antes de implementar

1. Quais dados são obrigatórios no cadastro e quais devem ser evitados por não serem usados?
2. Quais seções compõem sua anamnese e evolução? O que pode ficar vazio, e o que precisa de validação antes de encerrar?
3. O atendimento deve começar pela agenda, pelo paciente ou pelos dois? Como lidar com encaixe, retorno e atendimento sem agendamento?
4. Depois de encerrado, o registro deve ser imutável? Quem pode inserir adendo, imagem ou correção, e como isso deve aparecer na linha do tempo?
5. Quais tipos, tamanhos e origens de anexos são necessários? O clínico precisa comparar imagens ou apenas visualizar documentos?
6. O que recepção, profissional, administrador e outros profissionais podem ver, criar, alterar, compartilhar ou exportar?
7. É necessário prescrever, emitir atestado/solicitação de exame ou assinar digitalmente já na primeira versão?
8. Agenda, lembretes, financeiro, teleconsulta ou IA resolvem uma dor atual ou devem ser módulos posteriores?
9. Se houver IA, o paciente autoriza a escuta? O que deve ser rascunho, o que precisa de revisão e o que jamais pode ser salvo automaticamente?
10. Quais dados precisam ser exportados e em que formato se o consultório trocar de sistema?

## Referências

[1]: https://suporte.iclinic.com.br/pt-br/cadastro-de-um-paciente "Como cadastrar pacientes no Afya iClinic"
[2]: https://suporte.iclinic.com.br/pt-br/inicio-de-uma-consulta "Início de uma consulta"
[3]: https://iclinic.com.br/funcionalidades/prontuario-eletronico/ "Prontuário Eletrônico Personalizável | Afya iClinic"
[4]: https://suporte.iclinic.com.br/pt-br/adicionar-informacoes-pos-consulta "Como adicionar informações depois do término do atendimento?"
[5]: https://lps.iclinic.com.br/planos-e-precos/ "Planos e preços do iClinic"
[6]: https://iclinic.com.br/funcionalidades/inteligencia-artificial/ "Afya iClinic + IA"
