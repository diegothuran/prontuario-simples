# Operações da aplicação futura

Roteiro de backend/UI Django, não API publicada ou OpenAPI implementada. Forms server-side podem usar as mesmas operações via serviços internos. Rotas abaixo são proposta de nomes, não requisito de integração pública. CSRF e sessão em qualquer mutação, MFA/reautenticação conforme política. Repositório não tem login ou endpoints em execução.

| Operação proposta | Entrada do cliente | Política/saída |
|---|---|---|
| POST /patients | Campos administrativos homologados | Recepção/profissional autorizado; servidor gera clinic/id/local_number; sem CPF universal obrigatório |
| GET /patients | Termo/limite administrativo | DTO mínimo; sem texto clínico e sem varredura irrestrita |
| POST /appointments | Patient ID, profissional, intervalo | Mesma clínica, agenda autorizada e proteção de conflito transacional |
| POST /patients/{id}/encounters | Dados administrativos do atendimento | Profissional habilitado e vínculo ativo; servidor cria autoria/data de gravação |
| POST /encounters/{id}/drafts | Conteúdo inicial manual | Autor/contexto derivado da sessão; cria versão 1; contrato de criação refinado na TASK-007 |
| POST /drafts/{id}/update | draft-command schema | Autor de rascunho e versão; 409 se stale/status fechado |
| POST /drafts/{id}/finalize | finalize-command schema | Transação idempotente; retorna record-snapshot; não assina legalmente |
| POST /records/{id}/addenda | addendum-command schema | Mesmo autor e vínculo na v1; original preservado |
| GET /patients/{id}/timeline | Paginação | Vínculo clínico, escopo, autoria e auditoria; rascunhos só do próprio autor |
| POST /encounters/{id}/attachments | Multipart file + contexto mínimo | Profissional autorizado; tamanho/MIME/quarentena; upload protocol definido na POC |
| GET /attachments/{id}/download | ID | Check por objeto+estado clean+audit antes dos bytes; proxy; no-store |
| POST /copy-requests | Titular/representante, identidade e recorte | Pedido de acesso não exige justificativa clínica; verifica autoridade sem divulgar conteúdo à recepção |
| POST /copy-requests/{id}/exports | Recorte autorizado | Clinical/export permission explícita; job congelado; sem destinatário público arbitrário |
| GET /exports/{id}/download | ID | Revalidar identidade da sessão/autorização de entrega e expiração; não gera entrega pública |

A identidade do paciente/representante é verificada operacionalmente na solicitação de cópia; a v1 não cria portal de login de paciente ou integra e-mail/WhatsApp. Destinatário verificado e recibo de entrega ficam no processo da clínica. Poderes de representação não são provados por marcar um checkbox. Solicitação de terceiro/ordem judicial exige política específica e análise competente; não transformar em botão universal de download.

## Erros e retentativas

400 campo indevido/comando malformado; 401 sessão ausente ou inválida; 403 operação proibida sem divulgação; 404 recurso inexistente/inacessível por objeto, com comportamento consistente contra enumeração; 409 versão/estado/idempotência ou agenda conflitante; 413 arquivo grande; 415 formato não permitido; 422 inconsistência de domínio/campos; 503 dependência crítica indisponível. Respostas têm correlation_id e código estável, sem nota, nome de exame ou dados pessoais.

GET também registra auditoria de acesso clínico. Não prefetch de fichas clínicas para melhorar aparência. Form com 409 conserva texto e oferece comparação autorizada; logout/timeout não grava dados em localStorage. Falha de scan/backup/audit não é resolvida removendo a checagem.

## Constraints propostas no banco

UNIQUE clinic_id/local_number; FKs compostas ou equivalentes enforce de clínica/paciente entre Encounter/Draft/Attachment; final snapshot único por draft+version; idempotency unique por clinic+actor+operation+key com payload fingerprint; Draft version/status update condicionado; intervalo de agenda protegido contra corrida em PostgreSQL. Constraint implementada no banco e autorização server-side são complementares.

Não expor campos autoritativos via serializer genérico; não oferecer DELETE clínico; endpoint de admin não escreve snapshot. Os schemas de snapshot/attachment/export são resultados, nunca requests reutilizados por conveniência.
