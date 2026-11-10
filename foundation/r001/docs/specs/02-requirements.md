# 02 — Requisitos e critérios de aceite

r001: todos os requisitos abaixo são propostos. Prioridade crítica é um gate de segurança, não regra legal que inventamos. As fontes sustentam limites; detalhes de projeto são escolhas a validar.

Os aceites descrevem o aplicativo futuro. Nenhum deles foi executado apenas porque o pacote passou no validador.

## REQ-001 — critical

Operar inicialmente apenas com dados sintéticos e bloquear uso assistencial real até homologação clínica, de privacidade, assinatura e segurança do release.

**Aceite observável:** Ambiente demo claramente identificado; release real não é aprovado só por flag ou testes de schema.

**Cenário:** Tentar cadastrar paciente real ou ativar produção sem evidências de homologação.

**Origem:** proposta CLM-001 contextualizada por EVD-001. **Implementação:** TASK-001. **Eval:** EVAL-001.

## REQ-002 — critical

Usar contas individuais, sessão revogável, recuperação segura e MFA obrigatório antes de acesso clínico ou administrativo em uso real.

**Aceite observável:** Acesso sensível negado; recuperação não promove papel nem remove MFA silenciosamente; login não vaza existência de conta.

**Cenário:** Entrar sem segundo fator, reutilizar sessão revogada e simular recuperação sem prova de identidade.

**Origem:** proposta CLM-002 contextualizada por EVD-001. **Implementação:** TASK-003. **Eval:** EVAL-002.

## REQ-003 — critical

Aplicar autorização por objeto e vínculo assistencial no servidor, sem acesso clínico automático para recepção, administrador ou profissional sem vínculo.

**Aceite observável:** Nenhum conteúdo clínico ou metadado sensível é entregue; profissional vinculado tem apenas operações concedidas.

**Cenário:** Recepção, admin sem papel clínico e profissional sem vínculo tentam URL, busca, API e download de nota.

**Origem:** proposta CLM-003 contextualizada por EVD-012. **Implementação:** TASK-004. **Eval:** EVAL-003.

## REQ-004 — critical

Identificar o paciente por identificador interno, nome e data de nascimento, preservando homônimos e exigindo conferência antes de finalizar registros.

**Aceite observável:** Nenhuma mescla por nome/CPF; UI e backend mantêm patient_id e encounter_id corretos e solicitam conferência explícita.

**Cenário:** Criar dois homônimos, mudar de paciente com rascunho aberto e finalizar na ficha errada.

**Origem:** proposta CLM-004 contextualizada por EVD-003. **Implementação:** TASK-005. **Eval:** EVAL-004.

## REQ-005 — high

Manter agenda básica por profissional com estados explícitos, prevenção de sobreposição e atendimento sem agendamento, sem incluir texto clínico na agenda.

**Aceite observável:** Conflito não é salvo silenciosamente; histórico de reagendamento/cancelamento fica preservado; encontro avulso funciona.

**Cenário:** Agendar horários conflitantes, chegada, falta e atendimento avulso.

**Origem:** proposta CLM-005 contextualizada por EVD-001. **Implementação:** TASK-006. **Eval:** EVAL-005.

## REQ-006 — critical

Registrar atendimento manual com autoria, data de realização, horário do servidor e modelo de campos clínicos validado pela profissão antes de uso real.

**Aceite observável:** Finalização real bloqueada sem modelo/habilitação adequados; horário de gravação não é falsificado; não inventa conteúdo clínico.

**Cenário:** Modelo sem homologação, profissional inativo, dados retrospectivos e campos não observados.

**Origem:** proposta CLM-006 contextualizada por EVD-003. **Implementação:** TASK-007. **Eval:** EVAL-006.

## REQ-007 — critical

Salvar rascunho com confirmação persistida, controle otimista de versão e tratamento explícito de falha de conexão sem sobrescrita silenciosa.

**Aceite observável:** Segundo recebe 409 e conserva texto para reconciliação manual; UI nunca indica salvo sem commit confirmado.

**Cenário:** Dois navegadores editam versão 1; segundo grava após commit do primeiro; rede cai antes do retorno.

**Origem:** proposta CLM-007 contextualizada por EVD-001. **Implementação:** TASK-007. **Eval:** EVAL-007.

## REQ-008 — critical

Finalizar um único snapshot imutável por revisão, em transação idempotente, preservando conteúdo e autoria sem equiparar finalização a assinatura legal.

**Aceite observável:** Um snapshot e uma transação autoritativa; escrita posterior negada; signed não aceito; demo permanece not_implemented.

**Cenário:** Finalização concorrente/repetida, tentativa de editar finalized e envio de signed=true.

**Origem:** proposta CLM-008 contextualizada por EVD-004. **Implementação:** TASK-008. **Eval:** EVAL-008.

## REQ-009 — critical

Corrigir registros finalizados por adendos atribuídos, com motivo e vínculo ao original, sem apagar ou substituir o registro anterior.

**Aceite observável:** Original e adendo aparecem com datas/autores; atalho de sobrescrita e assinatura em nome do colega é negado.

**Cenário:** Retificação de informação após fechamento; outro autor tenta alterar original.

**Origem:** proposta CLM-009 contextualizada por EVD-002. **Implementação:** TASK-008. **Eval:** EVAL-009.

## REQ-010 — critical

Guardar anexos em storage privado, com validação de formato e tamanho, quarentena e inspeção antes da disponibilização, revalidando acesso a cada download.

**Aceite observável:** Objeto não fica público; estados de erro/quarentena não são acessíveis; somente arquivo clean e usuário autorizado recebem bytes.

**Cenário:** Arquivo falso .pdf, malware simulado, scanner indisponível e URL de outro paciente.

**Origem:** proposta CLM-010 contextualizada por EVD-006. **Implementação:** TASK-009. **Eval:** EVAL-010.

## REQ-011 — critical

Permitir cópia do prontuário ao titular ou representante verificado, sem exigir justificativa clínica, com exportação de recorte fiel e entrega controlada.

**Aceite observável:** Titular recebe cópia sem cobrança pelo acesso; terceiro não recebe; export não omite registros/falhas silenciosamente e expira cópia temporária.

**Cenário:** Titular pede cópia; terceiro sem poderes pede; export contém adendo e anexo indisponível.

**Origem:** proposta CLM-011 contextualizada por EVD-002. **Implementação:** TASK-010. **Eval:** EVAL-011.

## REQ-012 — critical

Registrar acessos e alterações relevantes em auditoria durável, protegida contra edição pelo usuário, sem copiar texto clínico para logs técnicos.

**Aceite observável:** Identidade, recurso, resultado e data ficam rastreáveis; falha bloqueia conteúdo/mutação conforme contingência; nenhum texto clínico é logado.

**Cenário:** Ler, negar acesso, finalizar, exportar e revogar usuário; serviço de auditoria falha.

**Origem:** proposta CLM-012 contextualizada por EVD-006. **Implementação:** TASK-011. **Eval:** EVAL-012.

## REQ-013 — critical

Manter backups protegidos de banco e documentos e comprovar restauração conjunta, incluindo vínculos, versões, auditoria e chaves necessárias.

**Aceite observável:** Dados e arquivos recuperados reconciliam IDs/hashes/permissões; RPO/RTO medidos e aprovados; backup sem restore não passa.

**Cenário:** Restaurar ambiente isolado após perda de banco e bucket e medir tempos/perdas.

**Origem:** proposta CLM-013 contextualizada por EVD-006. **Implementação:** TASK-012. **Eval:** EVAL-013.

## REQ-014 — critical

Não oferecer eliminação automática ou exclusão física de prontuários no MVP; tratar retenção, retificação e descarte por política validada e processo rastreável.

**Aceite observável:** Nenhum cron ou DELETE elimina conteúdo; solicitação segue análise competente; idade do registro não basta para descarte.

**Cenário:** Pedido de apagamento, desativação do paciente e registro com vinte anos.

**Origem:** proposta CLM-014 contextualizada por EVD-005. **Implementação:** TASK-011. **Eval:** EVAL-014.

## REQ-015 — critical

Manter IA clínica, diagnóstico automatizado, prescrição, cálculo de doses e classificação de urgência fora do produto inicial.

**Aceite observável:** Nenhuma ferramenta/endpoint/modelo executa essas ações; texto manual do profissional não é resultado da IA.

**Cenário:** Solicitar diagnóstico, interpretação de exame, dose ou receita gerada pelo sistema.

**Origem:** proposta CLM-015 contextualizada por EVD-007. **Implementação:** TASK-002. **Eval:** EVAL-015.

## REQ-016 — critical

Minimizar dados pessoais, proteger comunicação e segredos e impedir envio de prontuários para IA, analytics, prompts, repositório ou logs.

**Aceite observável:** TLS/headers/segredos adequados; nenhum PHI em terceiros, querystring, localStorage, telemetria ou mensagens de erro.

**Cenário:** Abrir página clínica, inspecionar tráfego/logs, erro HTTP, cache e payload de suporte.

**Origem:** proposta CLM-016 contextualizada por EVD-006. **Implementação:** TASK-011. **Eval:** EVAL-016.

## REQ-017 — high

Exibir identidade, autoria, status de salvamento e erros em interface acessível, responsiva e sem indicar ausência de achado quando o dado não foi registrado.

**Aceite observável:** Identidade sempre clara, labels/foco adequados; vazio é Não registrado, não Sem alergias; motion não oculta estados materiais.

**Cenário:** Usuário por teclado/celular, leitor de tela, slow network, alergia não registrada.

**Origem:** proposta CLM-017 contextualizada por EVD-002. **Implementação:** TASK-013. **Eval:** EVAL-017.

## REQ-018 — critical

Separar demo, homologação e produção, com manutenção, suporte, incidentes e plano de indisponibilidade atribuídos antes do uso real.

**Aceite observável:** Produção sem aceite e operação não liberada; retorno controlado preserva registros; responsáveis e plano de comunicação existem.

**Cenário:** Implantação sem responsável, rollback de release e exercício de incidente/indisponibilidade.

**Origem:** proposta CLM-018 contextualizada por EVD-008. **Implementação:** TASK-015. **Eval:** EVAL-018.

## REQ-019 — high

Apresentar histórico cronológico com origem, autor e versões, distinguindo registros clínicos, anexos, adendos e correções de cadastro.

**Aceite observável:** Timeline distingue instante assistencial e gravação; snapshot mantém identidade original com correção indicada; não muda autoria antiga.

**Cenário:** Adicionar registro retrospectivo e correção cadastral após snapshot.

**Origem:** proposta CLM-019 contextualizada por EVD-003. **Implementação:** TASK-008. **Eval:** EVAL-019.

## REQ-020 — critical

Derivar clínica, usuário e campos autoritativos do contexto do servidor, preservando isolamento entre recursos e rejeitando vínculos cruzados.

**Aceite observável:** Comandos fechados rejeitam campos indevidos; constraints e policy negam cross-clinic/patient; worker revalida autorização.

**Cenário:** Forjar clinic_id/author_id/scan status no body; associar nota de paciente A a encontro B.

**Origem:** proposta CLM-020 contextualizada por EVD-006. **Implementação:** TASK-004. **Eval:** EVAL-020.
