# 04 — Plano de implementação

Os cards são sequenciais por dependência, não cronograma contratado. Nada foi implementado aqui. TASK-001/002 definem escopo e campos; tarefas técnicas podem começar após decisão do recorte sintético. TASK-014/015 bloqueiam uso real.

Fase A: entrevista e recorte. Fase B: conta/permissões/cadastro. Fase C: agenda/registro/snapshot. Fase D: anexos/cópia/auditoria/restore. Fase E: revisão e eventual release homologado. Não estimar prazos sem conhecer disponibilidade e orçamento.

## TASK-001 — Definir profissão, consultório e responsáveis

Tipo: discovery. Requisitos: REQ-001, REQ-004, REQ-006, REQ-018. Dependências: nenhuma.

**Trabalho:** Definir profissão, consultório e responsáveis no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Entrevista sem dados reais; profissão, população, papéis, responsável clínico e revisor técnico identificados. Perguntas continuam abertas até resposta humana.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-002 — Congelar escopo e validar ficha com profissional

Tipo: discovery. Requisitos: REQ-001, REQ-006, REQ-015, REQ-017. Dependências: TASK-001.

**Trabalho:** Congelar escopo e validar ficha com profissional no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Ficha e campos obrigatórios revisados; finalização/assinatura/guarda e exclusões explicadas. Aprovação da r001 não inferida da conversa.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-003 — POC de contas, MFA e recuperação

Tipo: poc. Requisitos: REQ-002. Dependências: TASK-001.

**Trabalho:** POC de contas, MFA e recuperação no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Ambiente sintético; MFA, bloqueio de senha, revogação e recuperação adversarial; chaves MFA protegidas; revisão técnica das versões/dependências.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-004 — Construir permissões por objeto e constraints

Tipo: implementation. Requisitos: REQ-003, REQ-020. Dependências: TASK-003.

**Trabalho:** Construir permissões por objeto e constraints no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Permissões negativas/positivas testadas em PostgreSQL, URLs/DTOs/downloads/jobs; clínica e autor nunca vêm de input livre; concessão assistencial não autogerida.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-005 — Cadastro e identidade do paciente

Tipo: implementation. Requisitos: REQ-004, REQ-017. Dependências: TASK-004.

**Trabalho:** Cadastro e identidade do paciente no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Busca paginada, DOB/número local, homônimos, nome de preferência, revisão cadastral; campos clínicos não aparecem para recepção.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-006 — Agenda básica e atendimento avulso

Tipo: implementation. Requisitos: REQ-005. Dependências: TASK-005.

**Trabalho:** Agenda básica e atendimento avulso no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Estados/transições e conflitos de horários testados; sem integração de mensagens, convênio ou cobrança.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-007 — Rascunho manual, versões e falhas de rede

Tipo: implementation. Requisitos: REQ-006, REQ-007. Dependências: TASK-002, TASK-004, TASK-006.

**Trabalho:** Rascunho manual, versões e falhas de rede no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Revisões autorais e dois navegadores com 409 real; perda de rede sem confirmação falsa; não persistir PHI em localStorage.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-008 — Snapshots, adendos e timeline

Tipo: implementation. Requisitos: REQ-008, REQ-009, REQ-019. Dependências: TASK-007.

**Trabalho:** Snapshots, adendos e timeline no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Transaction/idempotência/race em PostgreSQL; original imutável inclusive sem CRUD no admin; adendos atribuídos; finalização não vira assinatura.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-009 — POC e implementação de anexos privados

Tipo: poc. Requisitos: REQ-010. Dependências: TASK-004, TASK-007.

**Trabalho:** POC e implementação de anexos privados no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Storage privado + scanner homologado; forged MIME/traversal/scan failed; revalidação no download; backup dos bytes disponível.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-010 — Cópia e exportação controlada

Tipo: implementation. Requisitos: REQ-011. Dependências: TASK-008, TASK-009.

**Trabalho:** Cópia e exportação controlada no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Verificação titular/representante, solicitação sem justificativa clínica; PDF/JSON/índice conferidos com clínico; permissão no download e expiração de cópia temporária.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-011 — Auditoria, dados e retenção

Tipo: implementation. Requisitos: REQ-012, REQ-014, REQ-016. Dependências: TASK-004.

**Trabalho:** Auditoria, dados e retenção no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Mutação+audit atômicas e leitura fail-closed; scan de logs/tráfego; contas DB segregadas; política de pedidos de dados e retenção revisada.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-012 — POC de backup e restauração

Tipo: poc. Requisitos: REQ-013. Dependências: TASK-008, TASK-009, TASK-011.

**Trabalho:** POC de backup e restauração no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Restaurar banco/bucket/audit/chaves em ambiente isolado e reconciliar hashes/IDs; medir RPO/RTO e aprovar contingência.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-013 — Revisão de fluxo e acessibilidade

Tipo: poc. Requisitos: REQ-017. Dependências: TASK-005, TASK-008, TASK-010.

**Trabalho:** Revisão de fluxo e acessibilidade no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Testes com teclado/celular/leitor de tela e parceiro clínico, fixtures fictícias; registrar dúvidas e falhas sem regravar resultados como aprovação.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-014 — Homologar assinatura e requisitos do conselho

Tipo: discovery. Requisitos: REQ-001, REQ-006, REQ-008. Dependências: TASK-002, TASK-008.

**Trabalho:** Homologar assinatura e requisitos do conselho no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Revisão profissional/jurídica da finalidade e assinatura/preservação; provedor real, verificação e documentação. Exige nova revisão de contratos se mudar not_implemented.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.

## TASK-015 — Revisão de segurança e decisão de piloto

Tipo: discovery. Requisitos: REQ-001, REQ-018. Dependências: TASK-010, TASK-011, TASK-012, TASK-013, TASK-014.

**Trabalho:** Revisão de segurança e decisão de piloto no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.

**Definição de pronto:** Engenheiro experiente revisa testes/superfícies; responsável clínico e de dados validam release; plano de incidente e suporte. Sem aceite, permanece sintético.

**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.
