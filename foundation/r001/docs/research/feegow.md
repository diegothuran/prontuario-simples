# Feegow Clinic como prontuário eletrônico para consultório brasileiro

**Data de referência:** 10/11/2026  
**Escopo:** pesquisa pública exclusivamente sobre o Feegow Clinic. Não houve login, criação de conta, teste de ambiente nem ação em dados.

## Leitura curta

O Feegow Clinic é apresentado como uma plataforma de gestão clínica cujo prontuário reúne cadastro do paciente, atendimento, formulários de anamnese/evolução, laudos, prescrições, textos/atestados, arquivos e imagens. A documentação pública também mostra integração com agenda e faturamento, permissões por usuário, pré-atendimento online e API. Para um prontuário simples de iniciante, o melhor aproveitamento é o núcleo clínico linear; a maior parte dos módulos de gestão deve ficar fora do primeiro escopo.

## Fluxo funcional observado na documentação pública

1. **Cadastro.** O usuário com a permissão “Cadastro Principal (Ficha)” acessa `Pacientes > Inserir`, preenche a ficha e salva. A edição pode ser feita por `Pacientes > Listar` ou pela Busca Rápida, usando nome, CPF ou contato. A inativação exige justificativa e o registro permanece localizável como inativo; a documentação também descreve reativação. [1]
2. **Atendimento e registro clínico.** Após iniciar o atendimento, o usuário com acesso aos formulários escolhe “inserir Anamnese/Evolução”, seleciona um modelo, preenche o pop-up e salva. O registro pode ser editado, impresso, compartilhado ou inativado com justificativa; registros inativos podem ser consultados e reativados. A Central de Ajuda menciona ainda laudos, formulários e curvas de evolução para acompanhamento de crescimento. [2]
3. **Histórico.** Enquanto insere ou abre anamnese/evolução, laudo/formulário, prescrição medicamentosa ou texto/atestado, existe a opção “Mostrar/Ocultar Histórico”. A lista é descrita como cronológica e pode reunir os tipos de registro citados, não apenas a tela atualmente aberta. [3]
4. **Anexos e imagens.** O prontuário possui a área “Arquivos”, com upload por escolha ou arrastar arquivo, além de ações para abrir, ampliar, girar, copiar link e excluir. A utilização depende da permissão “Arquivos diversos e vídeos”. A página de produto também declara arquivos centralizados e banco de imagens para exames. [4] [5]
5. **Pré-atendimento.** A Feegow documenta formulário online preenchido antes da consulta. Os tipos citados são Anamnese, Evolução e Formulário, mas a própria instrução recomenda usar “Formulário” para preenchimento pelo paciente, pois Anamnese e Evolução seriam destinados a profissionais. O link é enviado pelo sistema por e-mail, SMS ou WhatsApp e o conteúdo fica disponível no prontuário. [6]
6. **Acesso e controle.** A página inicial declara acesso pelo navegador, sem download ou instalação complicada, e a página do prontuário declara permissões de acesso para usuários. As páginas de ajuda confirmam que permissões específicas condicionam cadastro, formulários e arquivos. Isso demonstra que há controle de acesso documentado; não demonstra, por si só, a configuração correta de uma licença real. [4] [5] [7]

## Funcionalidades opcionais identificadas

- **Agenda:** gestão de agenda por profissionais e unidades; o prontuário declara integração com agenda e faturamento. [4] [7]
- **Prescrição e documentos:** receituário/prescrições integradas, emissão de atestados e pedidos de exame integrados à Mevo; a Central de Ajuda também trata prescrições como parte do histórico. [4] [3]
- **Financeiro e convênios:** a página inicial declara módulo financeiro e gestão de convênios, incluindo emissão automática de guia TISS. São módulos de gestão, não necessários para o primeiro prontuário simples. [7]
- **IA:** o Noa Notes é apresentado como recurso integrado que capta o áudio da consulta e gera resumo/anotações estruturadas para revisão, edição e validação final pelo médico. A página afirma redução de até 30% do tempo de registro; esse percentual é uma alegação comercial, não uma medição independente desta pesquisa. [8]
- **Integrações e telemedicina:** a Feegow declara integrações nativas, API e telemedicina com agenda, atendimento, prontuário, prescrição e financeiro. A existência de uma página ou declaração de integração não comprova compatibilidade com um sistema específico do consultório. [4] [7]
- **Personalização:** anamneses, evoluções e laudos por especialidade, formulários e gráficos personalizáveis são explicitamente anunciados. A Central de Ajuda confirma modelos/formulários e restrição por permissão; não foi testada a configuração de uma ficha. [2] [9]

## Segurança: o que foi verificado versus o que foi apenas declarado

**Verificado nesta pesquisa:** as páginas oficiais publicadas pela Feegow exibem declarações de prontuário “seguro”, permissões de usuários, operação 100% na nuvem, API, criptografia SSL, servidores AWS, conformidade com LGPD e certificação SBIS. Também foram lidos artigos públicos da Central de Ajuda que mostram permissões específicas e ações de inativação com justificativa. Isso verifica a presença dessas informações na documentação comercial e operacional pública, não a segurança efetiva da aplicação.

**Declarações comerciais não confirmadas de forma independente:** “conformidade com a LGPD”, “certificação SBIS” e seus níveis/versões, “nível de segurança mais alto”, segurança “de nível bancário”, operação em AWS, criptografia SSL e qualquer métrica de ganho da IA. Não foi feita auditoria técnica, análise de contrato/DPA, teste de controle de acesso, verificação de logs, backup/restauração, isolamento entre clínicas, retenção/eliminação, subcontratados ou consulta independente ao certificado. Portanto, não se deve presumir conformidade, certificação ou adequação ao consultório apenas com base no texto do site. [4] [7] [8]

## O que aproveitar em um prontuário simples

- Cadastro enxuto com busca por nome e identificador, edição e inativação justificada.
- Um fluxo evidente de atendimento: abrir paciente, inserir anamnese/evolução, salvar e consultar a linha histórica.
- Modelos de formulário por especialidade, mas com poucos campos obrigatórios e possibilidade de texto livre.
- Histórico cronológico que reúna os registros clínicos relevantes.
- Anexos separados de imagens, com visualização e exclusão controlada.
- Permissões mínimas por função, principalmente para cadastro, registro clínico e anexos.
- Registro de autoria, data/hora e motivo de inativação como requisito de implementação a confirmar, sem copiar a interface ou o código da Feegow.

## O que excluir da primeira versão para iniciante

Deixar fora do primeiro ciclo o financeiro completo, convênios/TISS, telemedicina, API, relatórios avançados, migração, banco de imagens sofisticado, pré-atendimento multicanal, prescrições integradas, Mevo, IA de áudio, curvas pediátricas e gestão de várias unidades. Esses recursos podem ser avaliados depois que o fluxo paciente → atendimento → anamnese/evolução → histórico → anexo estiver estável. Não há motivo para reproduzir a promessa de “mais de 200 funcionalidades” quando o objetivo é um prontuário simples. [7]

## O que perguntar ao clínico antes de especificar

- Quais campos são indispensáveis no cadastro e quais podem ser opcionais?
- O atendimento começa pela agenda, pela sala de espera ou diretamente pelo paciente?
- A anamnese e a evolução serão modelos separados? Quais seções e especialidades precisam de modelos próprios?
- Quem pode visualizar, editar, imprimir, compartilhar, anexar e inativar registros? A inativação deve exigir motivo e manter histórico de auditoria?
- O histórico deve mostrar todos os tipos de registro ou somente anamnese/evolução?
- Quais formatos e tamanhos de arquivo serão aceitos? Imagens e documentos terão categorias, pré-visualização e download?
- O consultório precisa de prescrição, atestado, pedido de exame, agenda, financeiro ou integração externa já no início?
- Há interesse em IA de áudio? Se sim, quem autoriza a captura, como o paciente é informado, quem revisa o texto e como o áudio/resumo é retido ou descartado?
- O sistema precisa funcionar apenas no navegador e em uma unidade, ou haverá múltiplos profissionais, locais e perfis de acesso?
- Quais exportações, backups, encerramento de prontuário e recuperação de dados são necessários? Essas respostas devem ser exigidas do fornecedor em contrato e demonstração, não inferidas do marketing.

## Referências

[1]: https://ajuda.feegow.com/support/solutions/articles/67000721167-4-como-cadastrar-editar-e-inativar-pacientes- "Como cadastrar, editar e inativar pacientes? — Central de Ajuda Feegow"
[2]: https://ajuda.feegow.com/support/solutions/articles/67000130171-2-como-inserir-e-inativar-anamneses-e-evolu%C3%A7%C3%B5es- "Como inserir e inativar Anamneses e Evoluções? — Central de Ajuda Feegow"
[3]: https://ajuda.feegow.com/support/solutions/articles/67000699513-visualizar-hist%C3%B3rico-de-atendimentos-enquanto-insere-ou-visualiza-informa%C3%A7%C3%B5es-no-prontu%C3%A1rio "Visualizar histórico de atendimentos no prontuário — Central de Ajuda Feegow"
[4]: https://ajuda.feegow.com/support/solutions/articles/67000143065-como-inserir-e-visualizar-os-arquivos-do-meu-paciente- "Como inserir e visualizar os arquivos do meu paciente? — Central de Ajuda Feegow"
[5]: https://feegowclinic.com.br/funcionalidades/prontuario "Prontuário eletrônico seguro e completo — Feegow Clinic"
[6]: https://ajuda.feegow.com/support/solutions/articles/67000700260-como-enviar-formul%C3%A1rio-de-pr%C3%A9-atendimento-ao-paciente- "Como enviar formulário de pré-atendimento ao paciente — Central de Ajuda Feegow"
[7]: https://feegowclinic.com.br/ "Feegow Clinic — Software para gestão de clínicas e centros médicos"
[8]: https://feegowclinic.com.br/blog/noa-notes-ia-para-prontuario-medico "IA para prontuário médico: saiba como funciona o Noa Notes no Feegow Clinic"
[9]: https://ajuda.feegow.com/support/solutions/articles/67000168703-4-como-configurar-formul%C3%A1rios-de-atendimento- "Como configurar formulários de atendimento — Central de Ajuda Feegow"
