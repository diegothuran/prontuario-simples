# Limites de saúde, privacidade e documentação

Data de consulta: 10/11/2026. Brasil. Esta análise técnica delimita requisitos para revisão; não é parecer jurídico, certificação nem autorização de uso clínico. A profissão, especialidade e instituição ainda não foram definidas. As referências do CFM descrevem o contexto médico; não aplicar automaticamente a psicologia, odontologia, enfermagem ou outras profissões.

## Dados de saúde e responsabilidade

A LGPD trata dados de saúde como dados pessoais sensíveis e prevê hipóteses específicas para seu tratamento no art. 11. Um checkbox genérico de “aceito a LGPD” não resolve base legal, finalidade, minimização ou segurança. A clínica precisa registrar quem decide o tratamento, quem opera os serviços e quais finalidades e contratos se aplicam. Consentimento para cuidado e consentimento para tratamento de dados são assuntos diferentes. [1]

A Lei 15.378/2026, Estatuto dos Direitos do Paciente, prevê confidencialidade no art. 15, nome de preferência no art. 10 e acesso ao prontuário, cópia sem ônus e solicitação de retificação no art. 19. Não exigir justificativa clínica do paciente para fornecer cópia; verificar sua identidade e, se houver representante, poderes e limites. Não substituir registros originais por uma retificação sem rastro. [2]

## Prontuário não é um bloco de notas

A Resolução CFM 1.638/2002 define prontuário como conjunto de informações, sinais e imagens sobre a saúde e a assistência, de caráter legal e sigiloso. O art. 5 trata identificação, anamnese, exame físico, exames, evolução, horários e identificação de profissionais, incluindo assinatura eletrônica. Os campos mínimos do protótipo não são um inventário completo de todos os campos obrigatórios do atendimento médico real. [3]

O protótipo pode usar texto livre organizado para aprender o fluxo. Antes de atendimento real, profissional responsável deve aprovar cadastro, modelo de registro e itens obrigatórios da profissão/especialidade. Não fabricar exame físico normal, negativas de sintomas, alergias ou diagnósticos para completar um modelo.

## Autoria, finalização e assinatura

A Resolução CFM 1.821/2007 consultada contém indicação de modificação pela Resolução 2.218/2018; seu art. 10 aparece revogado. Ela trata NGS2 e condições para eliminação da obrigatoriedade de registro em papel. Não afirmar que este pacote é certificado SBIS/CFM, atende integralmente NGS2 ou autoriza eliminar papel. [4]

A Lei 13.787/2018 exige integridade, autenticidade e confidencialidade na digitalização, reprodução das informações e certificado ICP-Brasil ou outro padrão legalmente aceito nesse processo. A destruição dos originais depende de condições e análise de comissão. Fazer upload de um PDF não cumpre, por si, essas condições. [5]

No contrato proposto, `finalized` significa snapshot fechado na aplicação. Login, data, hash, nome digitado e PDF exportado não equivalem automaticamente a assinatura eletrônica legalmente suficiente. O campo `signature_status: not_implemented` mantém esse limite explícito. Uso como prontuário assistencial definitivo, sem papel ou com descarte permanece bloqueado até homologação especializada da solução de assinatura e preservação aplicável. A homologação exige documentação do provedor e testes de autoria, certificado quando aplicável, verificação e preservação, não apenas mudança de um booleano.

## Guarda e exclusão

A Lei 13.787, art. 6, estabelece prazo mínimo de vinte anos a partir do último registro, inclusive para documentos originalmente eletrônicos, e condições para eliminação. Prazo mínimo não é autorização de limpeza automática. Normas específicas, litígios, valores históricos e políticas da instituição podem exigir tratamento adicional. A regra proposta do MVP é não oferecer exclusão física de prontuário; pedidos de retificação/eliminação seguem avaliação humana documentada. [5]

Não anunciar guarda permanente como regra universal nem apagar após vinte anos por cron job. A política definitiva e sua atualização são gate de uso real. Desativar cadastro não elimina histórico ou evidências.

## IA e finalidade

O MVP não usa IA em dados clínicos: não sugere diagnóstico, não interpreta exames, não gera receita, não calcula doses e não classifica urgência. O código pode ser produzido com assistência de IA usando apenas fontes e fixtures fictícias.

A RDC 657/2022 regula software como dispositivo médico e contempla exceções ligadas ao propósito. A finalidade e as funções efetivas, não a etiqueta “prontuário” ou uma aprovação humana superficial, orientam o enquadramento. Adicionar análise diagnóstica ou terapêutica exigirá revisão específica; supervisão humana não dispensa automaticamente regularização. [6]

## Segurança e incidentes

Além de impedir vazamento, o produto precisa manter integridade e disponibilidade do registro. Uma cópia de backup só é evidência útil depois de uma restauração controlada que recupere banco, arquivos, vínculos, permissões e versões.

A orientação oficial da ANPD atribui a comunicação de incidentes ao controlador quando houver riscos ou danos relevantes e prevê comunicação aos titulares além da ANPD. Plano operacional deve identificar responsáveis e procedimento atualizado; um operador técnico deve cooperar, sem assumir que enviar e-mail à clínica encerra suas obrigações. Prazos e conteúdo aplicáveis precisam ser revisados na regulamentação vigente antes do piloto. [7]

## Revisão antes do primeiro paciente real

É necessário um responsável clínico da profissão correta, apoio de engenharia para revisar segurança, validação de privacidade e contratos, mecanismo de assinatura/preservação adequado, acesso e cópia ao paciente, restore testado, plano de indisponibilidade e incidentes e registro de aceite do mesmo release. Sem isso, manter a aplicação em ambiente de teste com dados sintéticos. Não chamar um piloto com pacientes reais de “apenas POC” para dispensar essas condições.

## Referências

[1]: https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html "LGPD — texto atualizado na Câmara"
[2]: https://www2.camara.leg.br/legin/fed/lei/2026/lei-15378-6-abril-2026-798918-publicacaooriginal-178753-pl.html "Estatuto dos Direitos do Paciente — Lei 15.378/2026"
[3]: https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2002/1638_2002.pdf "CFM — Resolução 1.638/2002"
[4]: https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2007/1821_2007.pdf "CFM — Resolução 1.821/2007 com modificação indicada"
[5]: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13787.htm "Lei 13.787/2018 — digitalização e guarda"
[6]: https://www.gov.br/anvisa/en/rules-and-regulations/arquivos/rdc_657_2022-e.pdf/@@display-file/file "Anvisa — RDC 657/2022 em tradução publicada pela Agência"
[7]: https://www.gov.br/anpd/pt-br/assuntos/comunicacao-de-incidentes-de-seguranca-cis "ANPD — Comunicação de Incidente de Segurança"

## Complemento verificado em 2026

O [Parecer CFM 19/2026](https://portal.cfm.org.br/wp-content/uploads/2026/06/19_2026.pdf), páginas 2–4, reforça prazo mínimo, ausência de impedimento que imponha guarda superior, avaliação institucional, sigilo e termo formal de eliminação; recomenda cautela e rastreabilidade. Isso sustenta manter descarte fora do MVP. Não confundir seu escopo de consulta sobre descarte com certificação automática de qualquer sistema eletrônico.

O [Parecer CFM 12/2026](https://sistemas.cfm.org.br/normas/arquivos/pareceres/BR/2026/12_2026.pdf), páginas 5–6, trata principalmente entrega de prontuário a IML e explicita que ser médico não concede acesso irrestrito a pacientes sem vínculo legítimo. Não usamos o contexto pericial para exigir consentimento novo em toda leitura assistencial; usamos como apoio ao desenho de finalidade e vínculo. Regras específicas devem ser homologadas na clínica.

A seleção destas fontes não esgota legislação sanitária, ética, documental, acessibilidade, segurança ou particularidades de cada profissão. Mudanças futuras de norma e finalidade exigem revisão das specs e da operação.
