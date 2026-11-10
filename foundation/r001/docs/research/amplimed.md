# Amplimed como referência de prontuário eletrônico

**Data de referência:** 10/11/2026  
**Escopo:** páginas públicas oficiais da Amplimed. Não houve login, criação de conta, envio de formulário nem ação sobre dados de pacientes.

## O que a Amplimed declara oferecer

A Amplimed se apresenta como plataforma em nuvem para consultórios, clínicas e operadoras. Na página de prontuário, o fluxo comercial é uma demonstração solicitada por formulário com nome, e-mail profissional, telefone, função e número de profissionais da clínica. Isso é cadastro de lead, não prova do fluxo de cadastro de paciente dentro do produto. A mesma página declara migração de dados e preservação do histórico; porém não publica ali a sequência detalhada para criar um paciente novo. [1]

O fluxo clínico é organizado em três momentos: **antes da consulta**, **durante a consulta** e **depois da consulta**. Antes, a plataforma declara permitir consultar histórico, exames e documentos. Durante, declara oferecer campos personalizados por especialidade para formulários, anamneses, evoluções e protocolos, além de gráficos de exames e teleconsulta integrada. Depois, declara manter o histórico atualizado e permitir prescrição digital, emissão de atestados, exames e encaminhamentos com modelos e preenchimento automático. [1]

Para histórico, a página reúne evoluções, diagnósticos, prescrições e exames em um único lugar. Para anexos, afirma ser possível anexar e consultar exames, laudos e imagens diretamente no prontuário. A home acrescenta questionários que coletam dados antes do atendimento e os integram ao prontuário. [1] [2]

O acesso declarado é em nuvem, via internet, por profissionais autorizados, em múltiplos dispositivos e unidades. A home afirma oferecer login individual, perfis e permissões configuráveis, auditoria de acessos e registro das ações. Isso sugere uma capacidade importante para uma clínica pequena, mas não foi testado em ambiente autenticado. [1] [2]

## Funcionalidades opcionais e integrações declaradas

- **Agenda:** agendamento on-line, agenda integrada ao prontuário, confirmação e lembretes por WhatsApp, SMS ou e-mail, agenda por procedimento e assistente Amélia Agendamento. [1] [2]
- **Prescrição e documentos:** prescrição digital com base de medicamentos, modelos de documentos, assinatura digital certificada e integração divulgada com o Ampliprescreve. [1] [2]
- **Teleatendimento:** vídeo e prontuário no mesmo ambiente. [1] [2]
- **IA:** Amélia Transcrição transforma conversa em registro estruturado; Amélia Copilot permite buscar informações no histórico. A documentação pública informa que a transcrição é módulo adicional, ativado em configurações do prontuário, com cobrança conforme o pacote contratado. [2] [3]
- **Financeiro e convênios:** controle de pagamentos, módulo de pagamentos por link, NFS-e, repasses profissionais e faturamento TISS. A home direciona a solução a clínicas maiores e operadoras, portanto esses módulos não devem ser tratados como necessários para um consultório iniciante. [2]
- **Outras extensões:** dashboards, estoque, vacinas, pesquisa de satisfação, relatórios, comunicação e integrações do ecossistema AmpliSaúde. A página não detalha APIs, formatos de exportação ou integrações clínicas específicas. [2]

## Segurança: declaração comercial versus verificação

**Declarações públicas da Amplimed:** criptografia em trânsito TLS/SSL, backup automatizado, hospedagem AWS, redundância, recuperação de desastres, monitoramento contínuo, login individual, perfis e permissões, auditoria, DPO, portal do titular, gestão de consentimento, armazenamento protegido e assinatura digital certificada. A home também exibe referências a LGPD, ICP-Brasil, CFM e SSL Sectigo. [2]

**O que foi efetivamente verificado nesta pesquisa:** apenas que essas afirmações e selos aparecem no conteúdo público oficial consultado. Não foi realizada auditoria técnica, teste de criptografia, inspeção de logs, validação de backup/restauração, checagem de certificado, confirmação de escopo de uma eventual certificação ou revisão contratual. Portanto, não concluir que a Amplimed é conformidade LGPD, certificada ou “segura” em sentido independente; exigir evidências, escopo, datas, suboperadores, localização dos dados, SLA e procedimento de incidente antes de adotar qualquer promessa como requisito atendido.

## O que aproveitar em um prontuário simples

Aproveitar como **capacidades**, sem copiar marca, código ou design:

1. Um cadastro de paciente enxuto, com identificação e contatos, separado do registro clínico.
2. Um atendimento com sequência clara: queixa/anamnese, avaliação ou diagnóstico, conduta/plano e evolução.
3. Histórico cronológico pesquisável, com diagnósticos, prescrições, evoluções e exames visíveis sem trocar de módulo.
4. Anexos de exames, laudos e imagens ligados ao paciente e ao atendimento.
5. Campos e modelos personalizáveis, mas com poucos campos obrigatórios para não travar o iniciante.
6. Acesso individual por profissional e permissões mínimas; registrar quem criou, alterou ou finalizou um registro.
7. Agenda como módulo opcional e prescrição/documentos como extensões, não como pré-requisitos do primeiro uso.

## O que excluir da primeira versão para iniciantes

Deixar fora do núcleo inicial: faturamento TISS, NFS-e, repasses, estoque, vacinas, dashboards, marketing por e-mail, pesquisa de satisfação, operação multiunidade, operadoras, automação intensa de WhatsApp, telemedicina e IA de transcrição. São capacidades comerciais relevantes da plataforma, mas aumentam configuração, custo, riscos de permissão e carga de suporte. Também não incluir IA antes de definir consentimento, revisão obrigatória pelo clínico e política de retenção do áudio/transcrição.

## O que perguntar ao clínico antes de construir

- Quais dados são indispensáveis no cadastro e quais podem ficar opcionais?
- A anamnese e a evolução devem ser texto livre, campos estruturados ou ambos? Há modelos por especialidade?
- O que precisa aparecer na primeira tela do histórico: últimas evoluções, diagnósticos, medicamentos, exames ou alertas?
- Quais anexos serão aceitos, com que tamanho, e quem poderá visualizar, baixar ou excluir?
- Quem pode criar, editar, finalizar e corrigir uma evolução? Correções devem preservar o texto anterior e registrar motivo?
- Agenda e prescrição entram agora ou somente depois do prontuário básico?
- É necessária assinatura digital, emissão de atestado/encaminhamento ou exportação para o paciente?
- Quais perfis de acesso existem na rotina real: clínico, recepção, auxiliar e administrador?
- Se houver IA, o paciente será informado? O áudio será armazenado? O clínico revisará e aprovará o texto antes de salvar?
- Como o consultório pretende exportar, migrar, fazer backup e recuperar o histórico se trocar de sistema?

## Incertezas relevantes

O material público consultado não mostrou a tela real de cadastro de paciente, a ordem exata dos campos de uma consulta, regras de edição/finalização, limites de anexos, formatos de exportação, APIs, preços ou disponibilidade de cada módulo por plano. A documentação pública da Ampli IA confirma ativação e transcrição como módulo adicional, mas não permite verificar, sem acesso autenticado, o comportamento completo do recurso nem o tratamento do áudio. As afirmações de segurança acima permanecem declarações do fornecedor, não resultados de testes independentes.

## Referências

[1]: https://www.amplimed.com.br/prontuario-eletronico/ "Prontuário eletrônico para profissionais de saúde | Amplimed"

[2]: https://www.amplimed.com.br/ "Amplimed | Soluções para Clínicas e Profissionais da Saúde"

[3]: https://conhecimento.amplimed.com.br/configura%C3%A7%C3%A3o-ampli-ia-no-prontu%C3%A1rio "Ativando a Ampli IA no Prontuário | Conhecimento Amplimed"
