# HiDoctor como referência de prontuário eletrônico para consultório brasileiro

**Data de referência:** 10/11/2026  
**Escopo:** pesquisa exclusivamente em páginas oficiais do HiDoctor/Centralx. Não houve login, criação de conta, teste de produto ou ação em dados de pacientes.

## O que o HiDoctor descreve publicamente

O HiDoctor se apresenta como um prontuário para cadastro completo de pacientes, com ficha, foto, texto, anamneses organizadas por consulta e prescrições armazenadas na ficha. Também declara fichas personalizáveis para adaptar o atendimento à especialidade e à rotina do médico. [1] [2]

### Fluxo de cadastro e atendimento

O fluxo abaixo é uma **reconstituição do que as páginas públicas permitem identificar**; não é um fluxo testado na aplicação:

1. **Paciente:** criar ou localizar o prontuário e preencher dados pessoais, demográficos, contato, documentos, convênio e outros campos cadastrais. O changelog mostra relatórios baseados nesses grupos de dados, mas não publica todas as telas ou etapas de criação do cadastro. [5]
2. **Atendimento:** abrir o prontuário e registrar a consulta em uma ficha ou formulário personalizado. A anamnese é explicitamente organizada por consulta. Há também imagens, textos, prescrições e documentos associados ao paciente. [1] [2]
3. **Anamnese e síntese:** opcionalmente, o HiDoctor LIVE transcreve o áudio e produz resumo em SOAP ou Histórico Clínico; a Anamnese Inteligente organiza sintomas, medicamentos em uso, histórico familiar, doenças pregressas e alergias em blocos estruturados. O site também descreve o HiDoctor Neo como chat contextual para localizar informações, resumir históricos, fazer cálculos e gerar documentos. [1] [3]
4. **Histórico e retorno:** o histórico pode ser consultado por registros do prontuário e pela Busca Avançada, que o fornecedor afirma alcançar textos de formulários e PDFs anexados. O Neo também é descrito como capaz de localizar a última consulta, exames solicitados e outras informações. [2] [3]
5. **Anexos e imagens:** o sistema declara suporte a PDFs, Word e outros formatos, além de fotos capturadas no celular ou tablet e imagens/ilustrações associadas ao paciente. O changelog também descreve recuperação de registros e prontuários enviados ao Arquivo morto no HiDoctor Cloud. [1] [2] [5]

**Evolução:** as páginas consultadas falam em consultas, anamneses, histórico clínico, resumos e registros, mas não confirmam um campo ou fluxo separado chamado “evolução”. Para um produto iniciante, não se deve assumir que evolução seja diferente de registro de consulta sem validar com o clínico.

### Acesso e mobilidade

O fornecedor declara uso online e offline, software instalado no computador, HiDoctor NET/Cloud e aplicativo HiDoctor Mobile. Segundo a página pública, o aplicativo sincroniza os dados antes de permitir o uso sem internet; portanto, “offline” não significa sincronização instantânea nem acesso irrestrito a qualquer dado. O HiDoctor Capture é descrito como aplicativo separado para enviar fotos do celular à ficha. [1]

## Funcionalidades opcionais e periféricas

- **Agenda:** agenda de compromissos, agendamento online, confirmação e remarcação por WhatsApp, fila de adiantamento, bloqueios, duração de horários e acompanhamento do tempo de espera. [2] [5]
- **Prescrição:** receitas, atestados e pedidos de exame assinados digitalmente e enviados ao paciente por e-mail ou WhatsApp. A página específica também declara integração com o SNCR, obtenção de numeração e uso de certificado ICP-Brasil A3; esta é uma descrição do fornecedor, não uma validação independente de funcionamento ou de requisitos regulatórios. [2] [4]
- **Financeiro e gestão:** lançamento de serviços, materiais e medicamentos, contas do paciente, faturamento, regras de honorários, fluxo de caixa, estoque, repasses e relatórios gerenciais. O changelog descreve acesso ao faturamento pela agenda e às contas pelo prontuário. [2] [5]
- **IA:** transcrição, resumo SOAP/Histórico Clínico, organização da anamnese, busca contextual, cálculos, geração de documentos e sugestões de perguntas/exames. O próprio site informa créditos mensais e pacotes pagos; não foi testada precisão, retenção do áudio, revisão humana obrigatória ou explicabilidade. [3] [5]
- **Integrações e complementos:** HiDoctor Cloud/NET/Mobile/Capture, WhatsApp, MedBook, TUSS/CID, teleconsulta, TISS, chat interno, marketing, consentimentos, Atlas de Anatomia e BulasMed são divulgados como recursos da plataforma ou módulos relacionados. Eles ampliam o escopo, mas não são necessários para um prontuário simples. [2] [5]

## Segurança: declaração comercial versus verificação

**Declarações comerciais observadas:** o HiDoctor afirma confidencialidade dos dados clínicos, restrição de acesso da secretária, bloqueio de registros após edição, backups manuais, cópia em servidores mediante sincronia, padrões de segurança “de instituições bancárias” para acesso web e disponibilidade online/offline. [1] [2]

**Efetivamente verificado nesta pesquisa:** apenas a existência e o conteúdo dessas afirmações nas páginas públicas oficiais. Não foram testados login, perfis e permissões, bloqueio de edição, criptografia, logs, restauração, isolamento entre clínicas, exclusão, exportação, sincronização, aplicativo offline ou segurança da IA. Não foi presumida conformidade com LGPD, certificação ou validade operacional de qualquer controle.

## O que aproveitar em um prontuário simples

- Cadastro curto, pesquisável e progressivo, sem exigir todos os campos no primeiro contato.
- Registro de consultas em ordem cronológica, com distinção clara entre anamnese, exame/observação, avaliação, plano e retorno.
- Formulários personalizáveis, mas com um modelo inicial enxuto e editável.
- Histórico legível, busca por termos e visualização de anexos junto ao paciente.
- Anexos com tipo, data, origem e descrição; suporte inicial para PDF e imagem é suficiente.
- Acesso por papéis, trilha de alterações, exportação e backup claramente visíveis.
- Prescrição e agenda apenas como extensões independentes, ativadas quando o consultório realmente precisar.

Essas capacidades são referências funcionais, não instruções para copiar telas, código, textos ou marca do HiDoctor.

## O que excluir da primeira versão para iniciantes

Deixar fora do núcleo inicial: IA de transcrição/chat, créditos e sugestões clínicas; financeiro, estoque, repasses e TISS; marketing, campanhas e perfil público; telemedicina, MedBook e agendamento online; integrações com WhatsApp/SNCR; Atlas, calculadoras, BulasMed e recursos avançados de gestão. Também evitar começar com múltiplos modos offline, sincronização entre muitos dispositivos e dezenas de formulários de especialidade. Primeiro deve funcionar bem o ciclo **cadastrar → atender → salvar → localizar histórico → anexar → fazer backup**.

## O que perguntar ao clínico antes de especificar

1. Qual é o mínimo necessário no cadastro inicial e quais campos só aparecem no retorno?
2. Como o consultório diferencia primeira consulta, retorno, evolução e atendimento administrativo?
3. Quais partes da anamnese são obrigatórias e quais precisam ser personalizáveis por especialidade?
4. Quais formatos e tamanhos de anexos são usados hoje? Fotos precisam de comparação lado a lado ou apenas histórico?
5. Quem pode ver, criar, editar, assinar, excluir ou restaurar cada tipo de registro?
6. O médico precisa trabalhar sem internet? Em quais aparelhos e com quais dados disponíveis offline?
7. A prescrição deve ser apenas impressa, enviada digitalmente ou integrada a algum serviço externo?
8. Agenda e financeiro são necessidades do mesmo projeto ou devem permanecer separados do prontuário?
9. A IA é desejada? Em caso positivo, o que pode ser transcrito, o que exige revisão e por quanto tempo o áudio/resumo deve ser mantido?
10. Como o consultório fará backup, exportação, correção, arquivamento e recuperação de um prontuário?

## Referências

[1]: https://www.hidoctor.com.br/p/prontuario-eletronico/ "Prontuário Eletrônico - HiDoctor"
[2]: https://www.hidoctor.com.br/p/beneficios/ "Benefícios do HiDoctor"
[3]: https://www.hidoctor.com.br/p/inteligencia-artificial/ "Inteligência Artificial para transcrever, resumir e organizar consultas - HiDoctor"
[4]: https://www.hidoctor.com.br/p/prescricao/ "Prescrição digital integrada ao SNCR - HiDoctor"
[5]: https://changelog.hidoctor.com.br/Novidade "HiDoctor Changelog"
