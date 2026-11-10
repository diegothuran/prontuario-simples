# Decisões propostas — r001

Nenhuma ADR aprovada implicitamente. Registrar resposta humana e recorte antes de mudar status.

## DEC-001

Monólito Django + templates + PostgreSQL antes de SPA/microserviços.

Racional: Menos camadas e dependências para iniciante; versão LTS suportada; validar operação.

Requisitos: REQ-018. Status: proposed.

## DEC-002

Uma clínica por implantação, sem compartilhamento automático entre clínicas.

Racional: Reduz escopo sem dispensar isolamento e constraints.

Requisitos: REQ-003, REQ-020. Status: proposed.

## DEC-003

Separar finalização interna de assinatura homologada.

Racional: Snapshot/hash não prova assinatura legal; uso real exige decisão especializada.

Requisitos: REQ-001, REQ-008. Status: proposed.

## DEC-004

IA fora do prontuário inicial; implementação assistida apenas com dados fictícios.

Racional: Registro manual é suficiente para validar primeiro fluxo; IA clínica altera riscos e finalidade.

Requisitos: REQ-015, REQ-016. Status: proposed.

## DEC-005

Storage privado e acesso por proxy autenticado.

Racional: Revogar acesso no servidor; não dar URL pública/bearer permanente.

Requisitos: REQ-010, REQ-011. Status: proposed.

## DEC-006

Auth de biblioteca com MFA; não reinventar login.

Racional: Django e allauth são proposta a homologar, não garantia automática de segurança.

Requisitos: REQ-002. Status: proposed.
