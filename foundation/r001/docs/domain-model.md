# Domínio e estados

Todas as entidades e estados abaixo são propostas r001 para teste sintético, não norma clínica. As regras do atendimento real dependem de profissão e especialidade.

## Entidades

| Entidade | Responsabilidade e restrição |
|---|---|
| Clinic | Dono operacional do conjunto local; não une prontuários de outras clínicas |
| User/Membership | Conta individual, clínica, papéis explícitos, revogação e status MFA |
| ProfessionalProfile | Identificação profissional, conselho/UF/número e habilitação conferida; não verificada só pelo texto fornecido |
| Patient | Identidade administrativa, nome de preferência, DOB, número local e revisão; CPF opcional, sem mescla automática |
| CareGrant | Vínculo assistencial explícito, concessor autorizado, finalidade, validade, revogação; read/write conforme política |
| Appointment | Agenda sem detalhe clínico, paciente, profissional, início/fim e estado |
| Encounter | Atendimento com paciente/profissional e data de realização; pode não ter agendamento |
| DraftNote | Texto manual, versão e autor; vinculado a um encontro; edições preservam revisão |
| RecordSnapshot | Conteúdo fechado e atribuído, hash, horário do servidor e assinatura não implementada na demo |
| Addendum | Registro novo que referencia snapshot, motivo, autor e datas; não apaga original |
| Attachment | Metadados, bytes privados, proveniência e estados de inspeção |
| CopyRequest/ExportJob | Identidade/poderes verificados, recorte de registros, entrega autorizada, prazo e auditoria |
| AuditEvent | Quem acessou/finalizou/exportou/revogou, o quê, quando e resultado; sem texto clínico |

## Identificação e mínimo clínico

Cadastro do protótipo pede nome completo, data de nascimento e número local gerado; nome de preferência opcional. Guardar identidade administrativa separada do conteúdo clínico, inclusive respostas necessárias para a recepção. Correções cadastrais geram nova revisão e event; um snapshot antigo preserva a identidade considerada na finalização e exibe correções posteriores identificadas. Nenhuma fusão de homônimos na v1.

Para médico real, campos da Resolução CFM 1.638 não cabem integralmente no mínimo sintético. Sexo/dados de identificação aplicáveis, nome da mãe, naturalidade, endereço e conteúdo clínico pertinente devem ser discutidos e incluídos na baseline validada. Não inferir esses dados a partir do nome. Sem revisão da ficha, não habilitar uso real.

Nota textual proposta: queixa, história, observações/exame, avaliação manual e plano manual. Não preencher com “normal”, “nega” ou diagnóstico padrão quando não observado. Campos opcionais não são a declaração de ausência de um achado. `allergy_status` tem `not_recorded`, `none_reported`, `known`: somente o profissional registra declaração explícita e origem; não existe motor de alerta medicamentoso.

## Máquina de estados

Agenda: `scheduled → checked_in → completed`; `scheduled → cancelled/no_show`; cancelamento após chegada depende de encerramento administrativo do encontro e motivo, sem apagar notas. Na v1 não há reagendamento destrutivo: atualizar com histórico.

Encontro: `open → closed` ou `open → cancelled` sem conteúdo clínico finalizado. Cancelado com notas exige conservar registros e motivo; não reabrir snapshot. A rotina de fechamento confere que não há rascunho pendente. Desvincular agendamento não muda paciente/autor de um encontro com nota.

Nota: `draft → finalized`. Draft pode ter revisões; finalized não pode ser editada, apagada nem revertida para draft. Erro corrigido com adendo. Na v1, adendo do mesmo autor habilitado e com vínculo ativo; indisponibilidade do autor original exige novo registro separado, atribuído ao novo profissional e referência ao anterior, conforme fluxo a validar. Não permitir assinar em nome do colega.

Anexo: `quarantined → clean/rejected/scan_failed`. `clean` pode ser colocado em restricted por incidente; download revalida. Uploads temporários abandonados têm descarte operacional próprio, não se confunde com apagar documento clínico já incorporado. Implementador precisa registrar se/como anexo foi incorporado e classificar antes de aplicar limpeza.

Exportação: `pending → generating → ready/failed → expired`; export copia fontes, nunca transfere a única guarda. Nenhum atendimento é concluído porque exportou um PDF. Auditoria separa solicitação, preparação e entrega efetiva.

## Invariantes

Paciente/clínica/atendimento nunca mudam por edição de uma nota. Fechamento congela conteúdo e identidade; adendo mantém encadeamento. Alterar login/conselho do profissional não altera quem criou o registro histórico. Horário de atendimento informado pelo profissional e horário de gravação/finalização do servidor são distintos; correção retrospectiva tem motivo e não falsifica created_at.

Nenhuma entidade tem DELETE clínico em API/UI. Desativação não é eliminação. Retificação do titular pode ser revisão de cadastro, adendo clínico ou negativa fundamentada conforme análise competente; não é apagar a manifestação profissional silenciosamente.
