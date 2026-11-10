# Benchmark comparativo e recorte de escopo

## Objetivo e limite da leitura

Este relatório sintetiza, sem repetir pesquisa, os cinco conjuntos de resultados fornecidos sobre prontuários eletrônicos para consultórios no Brasil. A finalidade é orientar uma **proposta de MVP manual ambulatorial** para um consultório, com vários usuários e papéis de recepção, profissional e administração. **Não é aprovação do produto, especificação técnica, parecer jurídico ou afirmação de conformidade.**

A palavra “verificado” abaixo significa que a capacidade foi descrita nas páginas públicas oficiais ou na documentação oficial informada. Não houve login, teste funcional, criação de conta, auditoria independente, revisão contratual ou validação em dados reais. Alegações de LGPD, segurança, certificações, backups, criptografia, validade jurídica e integrações permanecem alegações dos fornecedores quando não acompanhadas de verificação independente nos dados fornecidos.

## Recomendação de recorte para o MVP

O núcleo inicial pode ser deliberadamente pequeno:

- cadastro e busca de pacientes;
- agenda básica do consultório;
- abertura de atendimento pelo profissional;
- formulário clínico curto, configurável com o clínico;
- salvamento do registro e consulta do histórico;
- anexação de exames, laudos ou imagens quando realmente necessário;
- acesso de vários usuários com os três papéis propostos: recepção, profissional e administração;
- fechamento do atendimento e tratamento explícito para correções posteriores, a validar com o clínico;
- administração básica de usuários, permissões e dados do consultório.

Para a primeira versão, recomenda-se deixar fora do corte: hospital, IA clínica ou transcrição, prescrição digital, telemedicina, integrações externas, faturamento/financeiro, convênios/TISS, marketing/mensageria, estoque, franquias/multiclínicas e automações avançadas. Esses itens aparecem nas ofertas pesquisadas, mas não são necessários para comprovar o valor do fluxo ambulatorial manual.

## Comparação rápida

| Fornecedor | Fluxos/capacidades públicas mais úteis ao núcleo | Complexidade anunciada que deve ficar fora do v1 | Leitura para a proposta |
|---|---|---|---|
| **Afya iClinic / iClinic** | Cadastro por recepção ou profissional, início pela agenda ou prontuário, campos configuráveis, histórico, anexos e regra documentada de encerramento com informação posterior preservando o original. | IA, prescrição, assinatura, teleconsulta, financeiro, mensageria e integrações. | É a referência mais clara, entre os cinco, para discutir o ciclo cadastrar → atender → encerrar → registrar informação posterior. |
| **Feegow Clinic** | Cadastro, busca, inativação/reativação, anamnese/evolução, histórico cronológico, arquivos, formulários e permissões específicas. | Pré-atendimento multicanal, IA, prescrição/atestados, faturamento, convênios/TISS, telemedicina, API e outros módulos. | Oferece bons exemplos de separação entre ficha, formulários clínicos, arquivos e permissões; o MVP pode usar somente o fluxo manual. |
| **Amplimed** | Histórico com evoluções, diagnósticos, prescrições e exames; anexos; campos personalizados; agenda integrada; perfis e permissões declarados. | IA, teleconsulta, financeiro, pagamentos, faturamento TISS, NFS-e, repasses e demais módulos. | Ajuda a validar a necessidade de uma ficha configurável e de anexos, mas a documentação pública não detalha suficientemente o fluxo para servir como regra pronta. |
| **Ninsaúde Clinic** | Formulários/protocolos personalizados, arquivos, alergias, documentos e agenda com check-in; acesso multiprofissional é anunciado. | IA, prescrição, teleconsulta, compartilhamento ampliado, multiclínicas, sessões/pacotes, marketing e automações. | Reforça a utilidade de formulários curtos, alergias e anexos; exige validação do fluxo de anamnese/evolução e das permissões antes de qualquer decisão. |
| **HiDoctor** | Ficha e foto, texto, anamneses por consulta, fichas personalizáveis, imagens, histórico, agenda e mobilidade anunciados. | IA, prescrição integrada, financeiro, estoque, teleconsulta, integrações regulatórias, offline/multiponto e gestão ampliada. | É uma referência para histórico por consulta e ficha personalizável, mas não comprova publicamente, nos dados fornecidos, perfis, bloqueios de edição ou logs. |

## Resultados por fornecedor

### 1. Afya iClinic / iClinic

**O que foi verificado nas fontes fornecidas.** A documentação de suporte descreve cadastro pela recepção em “Pacientes > Novo Paciente” e pelo profissional em “Prontuários > Novo Paciente”, com nome, data de nascimento, sexo e telefone como campos mínimos documentados. Também descreve início do atendimento pela agenda ou por prontuários, preenchimento, salvamento, encerramento e bloqueio de edição após finalizar. O produto anuncia prontuário personalizável, histórico, anexos e documentos. A documentação informa que uma informação ou imagem posterior pode ser adicionada com data e horário sem alterar o registro original. Acesso em computador, tablet e celular, perfis e permissões são anunciados.

**Aproveitamento no MVP.** Usar como referência de um percurso manual simples: recepção cadastra; profissional localiza ou abre o atendimento; profissional preenche e salva; o atendimento é encerrado; o histórico permanece consultável; eventual complemento posterior é registrado como novo evento ou anotação, sem substituir silenciosamente o anterior. Os campos clínicos, incluindo anamnese e evolução, ainda precisam ser definidos com o clínico.

**Fora do v1.** IA/transcrição, prescrição, assinatura, financeiro, teleconsulta, mensageria e integrações como WhatsApp, TISS, AWS e Glic. O foco não deve depender de iClinic Assist nem de qualquer outro módulo adicional.

**Pontos para validar.** Disponibilidade e preço por plano; detalhes de permissões; anexos e exportação; regras de correção após encerramento; e o conjunto mínimo de campos clínicos. A página de preços e a página de IA apresentam posicionamentos diferentes sobre a inclusão da IA, portanto isso não deve orientar o MVP.

**Links oficiais informados:** [Cadastro de paciente](https://suporte.iclinic.com.br/pt-br/cadastro-de-um-paciente) · [Início de uma consulta](https://suporte.iclinic.com.br/pt-br/inicio-de-uma-consulta) · [Prontuário eletrônico](https://iclinic.com.br/funcionalidades/prontuario-eletronico/) · [Informações pós-consulta](https://suporte.iclinic.com.br/pt-br/adicionar-informacoes-pos-consulta) · [Planos e preços](https://lps.iclinic.com.br/planos-e-precos/) · [IA](https://iclinic.com.br/funcionalidades/inteligencia-artificial/)

### 2. Feegow Clinic

**O que foi verificado nas fontes fornecidas.** A Central de Ajuda descreve cadastro, edição, busca, inativação com justificativa e reativação de pacientes. Descreve também inserção e inativação de anamnese/evolução, seleção de formulário, salvamento, edição e permissões de formulários. O histórico cronológico inclui atendimentos, anamnese/evolução, laudos/formulários, prescrições e textos/atestados. Há área de arquivos com upload e ações de visualização/manipulação, condicionada a permissão específica. Formulários de pré-atendimento podem ser enviados por e-mail, SMS ou WhatsApp. A página do produto anuncia permissões de usuários, agenda, faturamento, prescrições, API, telemedicina e Noa Notes.

**Aproveitamento no MVP.** A separação entre cadastro do paciente, formulário clínico, histórico e arquivos é uma boa referência para desenhar o fluxo sem exigir um pacote grande. A inativação com justificativa pode ser uma hipótese útil para discutir com o clínico e o administrador, mas não deve ser copiada como requisito sem confirmar a necessidade.

**Fora do v1.** Pré-atendimento online e envio por canais externos, Noa Notes/IA, prescrição e atestados, faturamento/financeiro, convênios/TISS, telemedicina, API e integrações. O MVP deve manter o preenchimento manual dentro do consultório.

**Pontos para validar.** Campos obrigatórios, permissões efetivamente disponíveis, limites e formatos de arquivos, retenção, restauração, exportação e histórico de alterações. Segurança, LGPD, certificações e demais declarações comerciais não foram auditadas.

**Links oficiais informados:** [Cadastro, edição e inativação](https://ajuda.feegow.com/support/solutions/articles/67000721167-4-como-cadastrar-editar-e-inativar-pacientes-) · [Anamneses e evoluções](https://ajuda.feegow.com/support/solutions/articles/67000130171-2-como-inserir-e-inativar-anamneses-e-evolu%C3%A7%C3%B5es-) · [Histórico de atendimentos](https://ajuda.feegow.com/support/solutions/articles/67000699513-visualizar-hist%C3%B3rico-de-atendimentos-enquanto-insere-ou-visualiza-informa%C3%A7%C3%B5es-no-prontu%C3%A1rio) · [Arquivos do paciente](https://ajuda.feegow.com/support/solutions/articles/67000143065-como-inserir-e-visualizar-os-arquivos-do-meu-paciente-) · [Prontuário](https://feegowclinic.com.br/funcionalidades/prontuario) · [Site do produto](https://feegowclinic.com.br/) · [Noa Notes](https://feegowclinic.com.br/blog/noa-notes-ia-para-prontuario-medico) · [Pré-atendimento](https://ajuda.feegow.com/support/solutions/articles/67000700260-como-enviar-formul%C3%A1rio-de-pr%C3%A9-atendimento-ao-paciente-)

### 3. Amplimed

**O que foi verificado nas fontes fornecidas.** A página de prontuário declara fluxo antes, durante e depois da consulta; histórico com evoluções, diagnósticos, prescrições e exames; anexos de exames, laudos e imagens; campos personalizados; agenda integrada; prescrição, documentos, teleconsulta e acesso em nuvem. A página principal declara login individual, perfis e permissões configuráveis, auditoria de acessos e registro de ações. Também declara módulos de financeiro, faturamento TISS, NFS-e, pagamentos e repasses. A documentação da Ampli IA informa que a transcrição de áudio é módulo adicional, ativado nas configurações e sujeito ao pacote contratado.

**Aproveitamento no MVP.** A proposta pode aproveitar somente as ideias de histórico, anexos, campos personalizados, agenda e acesso individual. O fluxo real de cadastro, a ordem dos campos, as regras de edição e a finalização não foram detalhados publicamente nos dados fornecidos, por isso não devem ser tratados como requisitos já resolvidos.

**Fora do v1.** Ampli IA, teleconsulta, prescrição, financeiro, pagamentos, faturamento TISS, NFS-e, repasses e qualquer integração ou migração que não seja necessária para o consultório inicial.

**Pontos para validar.** Sequência real do cadastro e atendimento; regras de edição/finalização; limites de anexos; formatos de exportação; disponibilidade por plano; e significado operacional de perfis, permissões, auditoria e registro de ações. As afirmações de segurança, LGPD, AWS, ICP-Brasil, CFM e SSL são apenas declarações comerciais no recorte fornecido.

**Links oficiais informados:** [Prontuário eletrônico](https://www.amplimed.com.br/prontuario-eletronico/) · [Soluções Amplimed](https://www.amplimed.com.br/) · [Ativação da Ampli IA](https://conhecimento.amplimed.com.br/configura%C3%A7%C3%A3o-ampli-ia-no-prontu%C3%A1rio)

### 4. Ninsaúde Clinic

**O que foi verificado nas fontes fornecidas.** A página de prontuário anuncia prontuários, prescrições, documentos, arquivos, formulários, alergias, protocolos personalizados e integração com Google Drive. A página de atendimento anuncia check-in, ficha cadastral, agenda online, agenda multiclínicas/multiprofissionais, retorno, bloqueio, sessões/pacotes e confirmações por SMS/WhatsApp. Também são anunciados teleconsulta, ditado, compartilhamento entre profissionais e cards com gráficos evolutivos, tags e CIDs. A página de segurança publica alegações sobre criptografia, backups, controles de acesso, monitoramento e alta disponibilidade, sem verificação independente no material fornecido.

**Aproveitamento no MVP.** Formulários curtos, ficha cadastral, histórico clínico, alergias e anexos podem ser apresentados ao clínico como hipóteses simples. Check-in e uma agenda básica podem ser considerados se o consultório realmente precisar deles desde o primeiro dia.

**Fora do v1.** Houdini/IA, prescrição, teleconsulta, compartilhamento ampliado, multiclínicas, sessões e pacotes, CRM/marketing, odontologia, integrações e automações de confirmação por canais externos.

**Pontos para validar.** Fluxo explícito de anamnese e evolução; campos obrigatórios; abertura e encerramento do atendimento; granularidade de permissões; organização de anexos; retenção, exportação e restauração. A pesquisa não verificou a IA, certificações, conformidade ou segurança operacional.

**Links oficiais informados:** [Prontuário eletrônico](https://www.ninsaude.com/pt-br/prontuario-eletronico-software-medico/) · [Sistema de atendimento](https://www.ninsaude.com/pt-br/sistema-de-atendimento-software-clinica/) · [Segurança](https://www.ninsaude.com/pt-br/seguranca/)

### 5. HiDoctor

**O que foi verificado nas fontes fornecidas.** A página de prontuário descreve ficha, foto, texto, prescrições armazenadas, anamneses organizadas por consulta, fichas personalizáveis, imagens e acesso online/offline. A página de benefícios lista histórico, assinatura digital, transcrição por IA, anexos, busca avançada, agenda, prescrição, gestão financeira, estoque, teleconsulta e mobilidade. A página de IA descreve HiDoctor LIVE, resumo SOAP/Histórico Clínico, Anamnese Inteligente e HiDoctor Neo. A página de prescrição declara integração com SNCR, assinatura e certificado ICP-Brasil A3. O changelog publica itens como arquivo morto, relatórios, gestão integrada ao prontuário/agenda, MedBook, WhatsApp e SNCR.

**Aproveitamento no MVP.** O histórico por consulta, a ficha personalizável, o texto manual, os anexos e a agenda são referências compatíveis com o núcleo desejado. A ideia de “cadastrar → atender → salvar → localizar histórico → anexar” pode ser usada para conversar com o clínico, sem assumir que todas as etapas foram testadas.

**Fora do v1.** IA, prescrição integrada, financeiro, estoque, telemedicina, integrações regulatórias, marketing/mensageria e a complexidade de uso offline/multiponto. O MVP deve começar com um único consultório e um fluxo online simples, caso isso seja confirmado como adequado ao uso real.

**Pontos para validar.** Perfis e permissões, bloqueios de edição, logs, sincronização, exportação, restauração, separação entre profissionais e definição de evolução. As páginas consultadas não confirmam um fluxo separado chamado “evolução”, nem verificam segurança, backup ou integrações em funcionamento.

**Links oficiais informados:** [Prontuário eletrônico](https://www.hidoctor.com.br/p/prontuario-eletronico/) · [Benefícios](https://www.hidoctor.com.br/p/beneficios/) · [Inteligência artificial](https://www.hidoctor.com.br/p/inteligencia-artificial/) · [Prescrição](https://www.hidoctor.com.br/p/prescricao/) · [Changelog](https://changelog.hidoctor.com.br/Novidade)

## Capacidades comuns e diferenças relevantes

### Capacidades que aparecem de forma recorrente

Os cinco materiais apontam para um núcleo semelhante: cadastro ou ficha de paciente; registro clínico com histórico; algum grau de personalização de formulários, fichas, anamneses ou evoluções; anexos, arquivos, exames, imagens ou documentos; e agenda ou atendimento integrado. Também aparecem repetidamente módulos adicionais de prescrição, IA, telemedicina, financeiro, mensageria e integrações.

Isso é uma **comparação de posicionamento e documentação pública**, não uma prova de que todos os produtos tenham a mesma implementação ou que os recursos estejam disponíveis no mesmo plano. Para o MVP, as capacidades recorrentes são sinais para validar com o clínico, não uma lista automática de requisitos.

### Diferenças que podem orientar perguntas, não decisões automáticas

- O iClinic documenta com mais clareza, no material fornecido, os pontos de abertura, encerramento e adição posterior sem alterar o registro original.
- O Feegow documenta com mais detalhe a separação entre cadastro, anamnese/evolução, histórico, arquivos e permissões específicas.
- A Amplimed declara perfis, permissões, auditoria de acessos e registro de ações, mas não detalha o fluxo interno nas páginas pesquisadas.
- O Ninsaúde destaca formulários/protocolos, alergias, arquivos e agenda de atendimento, mas deixa lacunas no fluxo de anamnese/evolução e nas permissões.
- O HiDoctor destaca anamneses organizadas por consulta, fichas personalizáveis e acesso online/offline, mas o material fornecido não confirma perfis, bloqueios de edição ou logs.

## Oportunidades simples ainda hipotéticas

As oportunidades abaixo são hipóteses de produto para testar com o clínico e a recepção; não são especificações técnicas nem promessas de conformidade:

1. **Fluxo de três passos visível:** cadastro/busca do paciente → atendimento do dia → histórico. Evita começar por módulos administrativos.
2. **Formulário clínico curto por padrão:** poucos campos definidos com o profissional, com possibilidade de ajustar nomes e ordem depois da validação do uso.
3. **Histórico legível por data e profissional:** mostrar os atendimentos em ordem e deixar claro o que é registro original e o que é complemento posterior.
4. **Anexos com contexto:** permitir que a equipe associe exame, laudo ou imagem ao paciente ou ao atendimento, sem ampliar o escopo para um gerenciador documental completo.
5. **Papéis explicados em linguagem de trabalho:** recepção cadastra e agenda; profissional registra o atendimento; administração gerencia usuários e configurações básicas. Os limites exatos devem ser definidos com os usuários.
6. **Inativação em vez de apagar sem contexto:** discutir se pacientes inativos e justificativas são necessários, sem copiar uma política de fornecedor antes de entender o processo do consultório.
7. **Demonstração sem módulos extras:** validar o MVP em uma situação ambulatorial manual, sem IA, prescrição, telemedicina, integração ou faturamento.
8. **Perguntas de encerramento:** testar com o clínico como corrigir uma informação após finalizar, quem pode visualizar cada registro e o que precisa aparecer no histórico.

## Questões mínimas antes de transformar a proposta em especificação

- Quais campos são indispensáveis no cadastro e no atendimento para a especialidade do consultório?
- A recepção poderá apenas cadastrar/agendar, ou também consultar parte do histórico? Qual parte?
- O profissional pode corrigir um atendimento encerrado? Se sim, como o consultório quer identificar a correção?
- Quais anexos são realmente usados e por quanto tempo precisam ser localizados?
- A agenda faz parte do primeiro dia ou o consultório pode começar somente com cadastro e atendimento?
- O que o papel administrativo precisa fazer além de gerenciar usuários e configurações básicas?
- Como tratar paciente inativo, duplicidade de cadastro e mudança de telefone?
- O que precisa ser exportado ou recuperado em uma troca de fornecedor? Essa pergunta exige validação específica, pois não foi confirmada nas fontes.

## Conclusão

Os cinco fornecedores convergem em um núcleo de prontuário e gestão ambulatorial, mas suas páginas também misturam esse núcleo com módulos avançados. Para um amigo não técnico iniciar um consultório, a proposta mais prudente é validar primeiro um fluxo manual, pequeno e observável: pacientes, agenda básica, atendimento, formulário curto, histórico, anexos necessários e três papéis de usuário. IA, prescrição, telemedicina e integrações devem permanecer fora do v1, não por serem inviáveis, mas porque não são necessárias para validar o problema inicial e não foram objeto de teste nesta pesquisa.
