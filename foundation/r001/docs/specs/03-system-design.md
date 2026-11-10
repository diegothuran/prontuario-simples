# 03 — Desenho de sistema

Proposta r001. Não há app, deploy, API em execução ou serviço externo configurado neste pacote.

## Escolha recomendada

Monólito modular Django 5.2 LTS, versão de correção suportada no início da implementação, Python compatível, PostgreSQL gerenciado e páginas HTML por templates Django. CSS próprio simples; JavaScript pontual para conflito, feedback e upload. Não começar com React + FastAPI + Kubernetes + microserviços: aumenta superfícies de falha e trabalho operacional sem evidência de necessidade. A documentação do Django lista suporte estendido da série 5.2 até abril de 2028; verificar o calendário no início do trabalho. [1]

Django auth/sessions e django-allauth MFA são a proposta de autenticação, com dependências pinadas depois da POC de compatibilidade. Usar fluxos da biblioteca, não criar algoritmo de senha/TOTP, JWT ou recuperação. A biblioteca documenta MFA; configuração segura e segredos exigem homologação e revisão. Alternativa OIDC gerenciado só se houver responsável por sua operação e vantagem comprovada na POC. [2]

## Componentes

```text
Navegador — TLS — Django (templates, sessão, CSRF, políticas)
                     |-- accounts: contas, convites, MFA, membros ativos
                     |-- patients: identificação e histórico de cadastro
                     |-- scheduling: agenda e encontros
                     |-- records: rascunhos, snapshots, adendos
                     |-- documents: quarentena, acesso e exportações
                     |-- audit: acessos e mutações
                     |-- operations: backup, incidentes, gates de implantação
                     |
                     +-- PostgreSQL privado
                     +-- storage privado (anexos, exportações, backup de arquivos)
                     +-- worker de inspeção de arquivos/exportação, se necessário
```

O worker não é microserviço de negócio. Pode ser processo separado do mesmo repositório. Jobs persistidos com estados pending/running/succeeded/failed; retomada idempotente. Redis/Celery não são requisito inicial: escolher apenas ao medir necessidade. Para demo, inspeção de arquivo pode usar stub declarado, que não habilita `clean` de produção.

## Implantação e confiança

Uma clínica por implantação no MVP. Mesmo assim usar `clinic_id` nos vínculos e constraints compostas; isso evita confusão e prepara evolução, mas não certifica multitenancy. Segunda clínica real exige nova validação de isolamento. Não reutilizar pacientes entre clínicas automaticamente.

O servidor deriva usuário e clínica da sessão e membership ativo consultado a cada operação. Nenhum body/form/header definido pelo cliente pode substituir autoria, papel, clinic_id, timestamps, status de assinatura, resultado de scan ou aprovação. Papéis são cumulativos apenas por concessão explícita; `admin` não herda `professional`.

Política de acesso por objeto: membership ativo + permissão da operação + vínculo assistencial ativo do profissional para o paciente; ser médico ou usuário da clínica não basta. Recepção lê apenas DTO administrativo. Downloads, busca, timeline, miniaturas, exportação e worker aplicam a mesma política. Não basta ocultar botão. A recepção pode preparar solicitação de cópia ao titular, mas não baixar conteúdo clínico.

Concessão de vínculo assistencial deve ter razão administrativa rastreável e validação do responsável clínico; usuário não pode se atribuir pacientes arbitrariamente. Demo usa vínculos criados pelo seed sintético. Não implementar acesso emergencial/break-glass na v1.

## Transações e concorrência

Paciente, encontro, nota e anexo vinculados na mesma clínica por FK/constraints, não só por comparação de strings. Escrever rascunho exige `expected_version`; update condicionado à versão/status e resposta 409 no conflito, sem sobrescrita silenciosa. Nada é confirmado como salvo antes do commit do servidor.

Finalizar: sessão/MFA e habilitação ativos; vínculo válido; autor do rascunho; atendimento aberto; versão esperada; campos revisados pelo profissional. Em transação: bloquear linha, congelar conteúdo, serializar versão canônica, calcular hash, fechar nota, registrar evento de auditoria e associação ao atendimento. Retentativas com a mesma chave e mesmo payload retornam mesmo resultado. Payload diferente na mesma chave retorna 409. Uma disputa entre duas finalizações produz um único snapshot.

Finalização não muda `signature_status` de `not_implemented`. Contrato de assinatura futura é nova revisão com evidência de provedor; não adicionar `signed=true` como atalho. Encerrar encontro requer nenhuma nota pendente e no mínimo um snapshot; agenda pode ser concluída na mesma transação. Cancelamento não remove histórico.

## Arquivos e exportações

Bucket não público. Objeto recebe chave aleatória sem nome/CPF. Upload autorizado, limite de bytes/MIME e detecção por conteúdo; PDF/JPEG/PNG propostos; rejeitar executáveis, SVG/HTML, arquivo protegido que impeça scan e traversal. Mesmo extensão válida não basta. `quarantined` permanece inacessível até inspeção terminar; scanner indisponível falha fechado. Hash e tamanho calculados pelo servidor.

Download via proxy autenticado, verificação por objeto em cada solicitação e `Cache-Control: no-store`, sem URL pública. Se futuramente houver URL assinada, documentar que acesso pode persistir até expiração; não prometer revogação imediata. Evitar embed de PDF ativo; download sanitizado/isolado com Content-Disposition attachment e `nosniff`.

Exportação é job autorizado por solicitação de cópia ou outro fundamento documentado, com lista congelada de snapshots/adendos/anexos clean, autoria e datas. Rascunhos não entram por padrão. Anexos indisponíveis são indicados; não omitir silenciosamente. PDF legível + JSON estruturado + índice/hashes dos anexos autorizados é proposta de portabilidade, não prescrição ou prova de assinatura. Revalidar permissões no download, expirar e apagar cópia temporária do export, não os registros fonte. Verificar identidade do titular/representante antes de entregar; titular não precisa dar justificativa para acessar seu próprio prontuário.

## Segurança operacional

Cookies Secure/HttpOnly/SameSite, CSRF, limite de tentativas, MFA obrigatório para contas clínicas/admin antes de uso real, sessões revogáveis, convite e recuperação sem enumeração. Django admin técnico sem CRUD de conteúdo finalizado; separar credencial de operação e auditar acesso excepcional autorizado. Criptografar segredos MFA usando estratégia homologada e chaves fora do banco; preservar recuperação de chaves em procedimento restrito.

TLS, criptografia em repouso, secrets manager, backups protegidos, conta DB da aplicação sem poder de remover auditoria/snapshots, migrations com revisão humana. Logs técnicos sem nomes, texto clínico, documentos, tokens ou payload de upload; registrar IDs e correlation_id. Sem analytics de terceiros em telas de paciente, sem cache de PHI no service worker/localStorage. Texto clínico escapado como texto, sem renderizar HTML arbitrário.

Escrita + audit event durável na mesma transação; falha impede mutação. Leitura clínica/download só entrega conteúdo após registro durável; falha indisponibiliza o recurso e aciona contingência, não ignora auditoria. Banco não é invulnerável a administradores privilegiados: export periódico de auditoria para armazenamento protegido, segregação de operação e alertas são necessários na homologação.

Backup inclui DB e bytes dos anexos, índice, versões e chaves necessárias, com retenções próprias. Targets propostos para negociar: RPO até 1 hora e RTO até 4 horas, não garantias. Configuração barata pode não atendê-los; medir restore. Plano de indisponibilidade usa processo clínico aprovado fora do app e reconciliação rastreável; não usar demo como contingência real.

## Fontes técnicas

[1]: https://www.djangoproject.com/download/ "Django — versões suportadas"
[2]: https://docs.allauth.org/en/latest/mfa/index.html "django-allauth — MFA"
