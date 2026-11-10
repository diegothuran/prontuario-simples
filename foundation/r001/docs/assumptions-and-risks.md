# Premissas e riscos

Adultos, ambulatório, uma clínica e atendimento manual são propostas, não validações de mercado. Os cinco concorrentes são amostra orientadora e suas funcionalidades são declarações públicas, não auditoria. Consultar limites e perguntas. Não foi identificado conflito documental do usuário: ele não forneceu ficha/fluxo clínico. As diferenças entre escopo mínimo e campos normativos permanecem Q-001/Q-004, não foram escondidas.

## RSK-001 — critical

Registro no paciente errado

Requisitos: REQ-004, REQ-020.

Mitigação proposta: Identidade persistente na tela, IDs imutáveis, constraints e conferência explícita antes de finalizar. Ainda exige avaliação.

## RSK-002 — critical

Vazamento por papéis, URLs ou workers

Requisitos: REQ-003, REQ-010, REQ-011, REQ-020.

Mitigação proposta: Política por objeto, negação por padrão, proxy autorizado, teste adversarial. Ainda exige avaliação.

## RSK-003 — critical

Perda/sobrescrita do conteúdo ou autoria

Requisitos: REQ-007, REQ-008, REQ-009, REQ-019.

Mitigação proposta: Versions, transação, idempotência, snapshot imutável, adendos e restore. Ainda exige avaliação.

## RSK-004 — critical

Finalização confundida com assinatura ou certificação

Requisitos: REQ-001, REQ-006, REQ-008.

Mitigação proposta: UI e contrato não alegam validade; revisão profissional e assinatura homologada em nova revisão. Ainda exige avaliação.

## RSK-005 — critical

Backup incompleto e interrupção da assistência

Requisitos: REQ-013, REQ-018.

Mitigação proposta: DB+objetos+chaves, ensaio de restauração e contingência profissional. Ainda exige avaliação.

## RSK-006 — critical

Dados sensíveis enviados a terceiros/IA ou publicados em Git

Requisitos: REQ-015, REQ-016.

Mitigação proposta: Dados fictícios, minimização, revisão logs/tráfego/artefatos e sem IA no produto v1. Ainda exige avaliação.

## RSK-007 — critical

Iniciante deploya demo como sistema clínico

Requisitos: REQ-001, REQ-018.

Mitigação proposta: Guia acessível, bloqueios explícitos, engenheiro e responsável clínico antes de dados reais. Ainda exige avaliação.

## RSK-008 — critical

Consentimento genérico, retenção/descarte e direitos tratados incorretamente

Requisitos: REQ-011, REQ-014, REQ-016.

Mitigação proposta: Política de dados profissional, titular/representante verificados, sem DELETE/cleanup clínico. Ainda exige avaliação.
