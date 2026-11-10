"""Materializa o modelo r001 e documentos de rastreabilidade; sem IA, rede ou aplicação."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCOPE = 'Fundação proposta de registro clínico manual ambulatorial; desenvolvimento sintético e gate separado de uso real'


def save(rel, obj):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def text(rel, value):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value.rstrip() + '\n', encoding='utf-8')


# Enunciados são propostas do produto. Fontes normativas sustentam limites, não todos os detalhes.
DEFINITIONS = [
    ('critical', 'Operar inicialmente apenas com dados sintéticos e bloquear uso assistencial real até homologação clínica, de privacidade, assinatura e segurança do release.', '001', '001', 'Tentar cadastrar paciente real ou ativar produção sem evidências de homologação.', 'Ambiente demo claramente identificado; release real não é aprovado só por flag ou testes de schema.'),
    ('critical', 'Usar contas individuais, sessão revogável, recuperação segura e MFA obrigatório antes de acesso clínico ou administrativo em uso real.', '001', '003', 'Entrar sem segundo fator, reutilizar sessão revogada e simular recuperação sem prova de identidade.', 'Acesso sensível negado; recuperação não promove papel nem remove MFA silenciosamente; login não vaza existência de conta.'),
    ('critical', 'Aplicar autorização por objeto e vínculo assistencial no servidor, sem acesso clínico automático para recepção, administrador ou profissional sem vínculo.', '012', '004', 'Recepção, admin sem papel clínico e profissional sem vínculo tentam URL, busca, API e download de nota.', 'Nenhum conteúdo clínico ou metadado sensível é entregue; profissional vinculado tem apenas operações concedidas.'),
    ('critical', 'Identificar o paciente por identificador interno, nome e data de nascimento, preservando homônimos e exigindo conferência antes de finalizar registros.', '003', '005', 'Criar dois homônimos, mudar de paciente com rascunho aberto e finalizar na ficha errada.', 'Nenhuma mescla por nome/CPF; UI e backend mantêm patient_id e encounter_id corretos e solicitam conferência explícita.'),
    ('high', 'Manter agenda básica por profissional com estados explícitos, prevenção de sobreposição e atendimento sem agendamento, sem incluir texto clínico na agenda.', '001', '006', 'Agendar horários conflitantes, chegada, falta e atendimento avulso.', 'Conflito não é salvo silenciosamente; histórico de reagendamento/cancelamento fica preservado; encontro avulso funciona.'),
    ('critical', 'Registrar atendimento manual com autoria, data de realização, horário do servidor e modelo de campos clínicos validado pela profissão antes de uso real.', '003', '007', 'Modelo sem homologação, profissional inativo, dados retrospectivos e campos não observados.', 'Finalização real bloqueada sem modelo/habilitação adequados; horário de gravação não é falsificado; não inventa conteúdo clínico.'),
    ('critical', 'Salvar rascunho com confirmação persistida, controle otimista de versão e tratamento explícito de falha de conexão sem sobrescrita silenciosa.', '001', '007', 'Dois navegadores editam versão 1; segundo grava após commit do primeiro; rede cai antes do retorno.', 'Segundo recebe 409 e conserva texto para reconciliação manual; UI nunca indica salvo sem commit confirmado.'),
    ('critical', 'Finalizar um único snapshot imutável por revisão, em transação idempotente, preservando conteúdo e autoria sem equiparar finalização a assinatura legal.', '004', '008', 'Finalização concorrente/repetida, tentativa de editar finalized e envio de signed=true.', 'Um snapshot e uma transação autoritativa; escrita posterior negada; signed não aceito; demo permanece not_implemented.'),
    ('critical', 'Corrigir registros finalizados por adendos atribuídos, com motivo e vínculo ao original, sem apagar ou substituir o registro anterior.', '002', '008', 'Retificação de informação após fechamento; outro autor tenta alterar original.', 'Original e adendo aparecem com datas/autores; atalho de sobrescrita e assinatura em nome do colega é negado.'),
    ('critical', 'Guardar anexos em storage privado, com validação de formato e tamanho, quarentena e inspeção antes da disponibilização, revalidando acesso a cada download.', '006', '009', 'Arquivo falso .pdf, malware simulado, scanner indisponível e URL de outro paciente.', 'Objeto não fica público; estados de erro/quarentena não são acessíveis; somente arquivo clean e usuário autorizado recebem bytes.'),
    ('critical', 'Permitir cópia do prontuário ao titular ou representante verificado, sem exigir justificativa clínica, com exportação de recorte fiel e entrega controlada.', '002', '010', 'Titular pede cópia; terceiro sem poderes pede; export contém adendo e anexo indisponível.', 'Titular recebe cópia sem cobrança pelo acesso; terceiro não recebe; export não omite registros/falhas silenciosamente e expira cópia temporária.'),
    ('critical', 'Registrar acessos e alterações relevantes em auditoria durável, protegida contra edição pelo usuário, sem copiar texto clínico para logs técnicos.', '006', '011', 'Ler, negar acesso, finalizar, exportar e revogar usuário; serviço de auditoria falha.', 'Identidade, recurso, resultado e data ficam rastreáveis; falha bloqueia conteúdo/mutação conforme contingência; nenhum texto clínico é logado.'),
    ('critical', 'Manter backups protegidos de banco e documentos e comprovar restauração conjunta, incluindo vínculos, versões, auditoria e chaves necessárias.', '006', '012', 'Restaurar ambiente isolado após perda de banco e bucket e medir tempos/perdas.', 'Dados e arquivos recuperados reconciliam IDs/hashes/permissões; RPO/RTO medidos e aprovados; backup sem restore não passa.'),
    ('critical', 'Não oferecer eliminação automática ou exclusão física de prontuários no MVP; tratar retenção, retificação e descarte por política validada e processo rastreável.', '005', '011', 'Pedido de apagamento, desativação do paciente e registro com vinte anos.', 'Nenhum cron ou DELETE elimina conteúdo; solicitação segue análise competente; idade do registro não basta para descarte.'),
    ('critical', 'Manter IA clínica, diagnóstico automatizado, prescrição, cálculo de doses e classificação de urgência fora do produto inicial.', '007', '002', 'Solicitar diagnóstico, interpretação de exame, dose ou receita gerada pelo sistema.', 'Nenhuma ferramenta/endpoint/modelo executa essas ações; texto manual do profissional não é resultado da IA.'),
    ('critical', 'Minimizar dados pessoais, proteger comunicação e segredos e impedir envio de prontuários para IA, analytics, prompts, repositório ou logs.', '006', '011', 'Abrir página clínica, inspecionar tráfego/logs, erro HTTP, cache e payload de suporte.', 'TLS/headers/segredos adequados; nenhum PHI em terceiros, querystring, localStorage, telemetria ou mensagens de erro.'),
    ('high', 'Exibir identidade, autoria, status de salvamento e erros em interface acessível, responsiva e sem indicar ausência de achado quando o dado não foi registrado.', '002', '013', 'Usuário por teclado/celular, leitor de tela, slow network, alergia não registrada.', 'Identidade sempre clara, labels/foco adequados; vazio é Não registrado, não Sem alergias; motion não oculta estados materiais.'),
    ('critical', 'Separar demo, homologação e produção, com manutenção, suporte, incidentes e plano de indisponibilidade atribuídos antes do uso real.', '008', '015', 'Implantação sem responsável, rollback de release e exercício de incidente/indisponibilidade.', 'Produção sem aceite e operação não liberada; retorno controlado preserva registros; responsáveis e plano de comunicação existem.'),
    ('high', 'Apresentar histórico cronológico com origem, autor e versões, distinguindo registros clínicos, anexos, adendos e correções de cadastro.', '003', '008', 'Adicionar registro retrospectivo e correção cadastral após snapshot.', 'Timeline distingue instante assistencial e gravação; snapshot mantém identidade original com correção indicada; não muda autoria antiga.'),
    ('critical', 'Derivar clínica, usuário e campos autoritativos do contexto do servidor, preservando isolamento entre recursos e rejeitando vínculos cruzados.', '006', '004', 'Forjar clinic_id/author_id/scan status no body; associar nota de paciente A a encontro B.', 'Comandos fechados rejeitam campos indevidos; constraints e policy negam cross-clinic/patient; worker revalida autorização.'),
]

TASKS = [
    ('001', 'Definir profissão, consultório e responsáveis', 'discovery', [1, 4, 6, 18], [], 'Entrevista sem dados reais; profissão, população, papéis, responsável clínico e revisor técnico identificados. Perguntas continuam abertas até resposta humana.'),
    ('002', 'Congelar escopo e validar ficha com profissional', 'discovery', [1, 6, 15, 17], ['001'], 'Ficha e campos obrigatórios revisados; finalização/assinatura/guarda e exclusões explicadas. Aprovação da r001 não inferida da conversa.'),
    ('003', 'POC de contas, MFA e recuperação', 'poc', [2], ['001'], 'Ambiente sintético; MFA, bloqueio de senha, revogação e recuperação adversarial; chaves MFA protegidas; revisão técnica das versões/dependências.'),
    ('004', 'Construir permissões por objeto e constraints', 'implementation', [3, 20], ['003'], 'Permissões negativas/positivas testadas em PostgreSQL, URLs/DTOs/downloads/jobs; clínica e autor nunca vêm de input livre; concessão assistencial não autogerida.'),
    ('005', 'Cadastro e identidade do paciente', 'implementation', [4, 17], ['004'], 'Busca paginada, DOB/número local, homônimos, nome de preferência, revisão cadastral; campos clínicos não aparecem para recepção.'),
    ('006', 'Agenda básica e atendimento avulso', 'implementation', [5], ['005'], 'Estados/transições e conflitos de horários testados; sem integração de mensagens, convênio ou cobrança.'),
    ('007', 'Rascunho manual, versões e falhas de rede', 'implementation', [6, 7], ['002', '004', '006'], 'Revisões autorais e dois navegadores com 409 real; perda de rede sem confirmação falsa; não persistir PHI em localStorage.'),
    ('008', 'Snapshots, adendos e timeline', 'implementation', [8, 9, 19], ['007'], 'Transaction/idempotência/race em PostgreSQL; original imutável inclusive sem CRUD no admin; adendos atribuídos; finalização não vira assinatura.'),
    ('009', 'POC e implementação de anexos privados', 'poc', [10], ['004', '007'], 'Storage privado + scanner homologado; forged MIME/traversal/scan failed; revalidação no download; backup dos bytes disponível.'),
    ('010', 'Cópia e exportação controlada', 'implementation', [11], ['008', '009'], 'Verificação titular/representante, solicitação sem justificativa clínica; PDF/JSON/índice conferidos com clínico; permissão no download e expiração de cópia temporária.'),
    ('011', 'Auditoria, dados e retenção', 'implementation', [12, 14, 16], ['004'], 'Mutação+audit atômicas e leitura fail-closed; scan de logs/tráfego; contas DB segregadas; política de pedidos de dados e retenção revisada.'),
    ('012', 'POC de backup e restauração', 'poc', [13], ['008', '009', '011'], 'Restaurar banco/bucket/audit/chaves em ambiente isolado e reconciliar hashes/IDs; medir RPO/RTO e aprovar contingência.'),
    ('013', 'Revisão de fluxo e acessibilidade', 'poc', [17], ['005', '008', '010'], 'Testes com teclado/celular/leitor de tela e parceiro clínico, fixtures fictícias; registrar dúvidas e falhas sem regravar resultados como aprovação.'),
    ('014', 'Homologar assinatura e requisitos do conselho', 'discovery', [1, 6, 8], ['002', '008'], 'Revisão profissional/jurídica da finalidade e assinatura/preservação; provedor real, verificação e documentação. Exige nova revisão de contratos se mudar not_implemented.'),
    ('015', 'Revisão de segurança e decisão de piloto', 'discovery', [1, 18], ['010', '011', '012', '013', '014'], 'Engenheiro experiente revisa testes/superfícies; responsável clínico e de dados validam release; plano de incidente e suporte. Sem aceite, permanece sintético.'),
]

QUESTIONS = [
    ('Qual profissão e especialidade utilizarão o prontuário e quem revisará seus campos e regras?', True),
    ('O primeiro público é adulto, ambulatorial, de uma única clínica? Há menores, representantes ou sigilo específico que invalidem o recorte?', True),
    ('Quem é o responsável clínico e quem revisará engenharia, privacidade e contratos antes de pacientes reais?', True),
    ('Qual mecanismo de assinatura/preservação será homologado para o uso pretendido, e haverá convivência com papel?', True),
    ('Qual orçamento mensal, hospedagem, storage, localização dos dados, operadores e responsáveis pela manutenção?', True),
    ('Quais RPO/RTO e procedimento de indisponibilidade são aceitáveis e como serão medidos em restauração?', True),
    ('Quem pode conceder vínculo assistencial e preparar/entregar cópia a titular ou representante, e como comprovar autoridade?', True),
    ('Agenda, anexos e exportação são essenciais já na primeira demo, ou haverá uma sequência menor de validação?', False),
    ('Qual nome/identidade visual e como é o computador/conexão usados pelo consultório?', False),
]

EXTRA_CASES = [
    ([2, 3], 'Sessão e vínculo revogados durante navegação', 'Após login, revogar membership/care grant e repetir read/download/finalize.', 'Solicitação seguinte é negada no servidor; frontend limpo não é única defesa.', 'critical'),
    ([3, 20], 'Isolamento por objeto em listagem e worker', 'Dois conjuntos fictícios A/B e usuário A; pesquisar, exportar e manipular IDs B.', 'Nem bytes, nem título clínico, nem contagem indevida; worker valida escopo novamente.', 'critical'),
    ([8], 'Idempotência com payload diferente', 'Duas finalizações com mesma chave mas expected_version diferente.', 'Segunda operação 409; original não é alterado; nenhum novo snapshot.', 'critical'),
    ([7], 'Expiração de sessão com texto ainda na tela', 'Digitar; expirar sessão; salvar; autenticar novamente.', 'Nunca exibe Salvo sem commit; texto é reconciliado pelo usuário sem cache persistente de PHI.', 'critical'),
    ([10], 'Revogação de acesso a arquivo já exportado', 'Revogar usuário antes de download de export ready.', 'Proxy recusa nova entrega; cópia já baixada não pode ser revogada magicamente e isso é informado.', 'critical'),
    ([11, 19], 'Fidelidade do pacote de cópia', 'Snapshot A, dois adendos, arquivo clean e outro scan_failed.', 'PDF/JSON/índice coerentes; datas/autor/conteúdo mantidos; arquivo não entregue é claramente indicado.', 'critical'),
    ([12], 'Transação clínica interrompida', 'Falhar insert de audit durante finalização.', 'Rollback; nenhuma nota finalized sem evento durável; retentativa não duplica.', 'critical'),
    ([12, 16], 'Exposição de dados por telemetria e erros', 'Provocar erro com nota e documento; inspecionar logs e requests.', 'Sem conteúdo clínico, token, filename identificável ou PII em terceiros/logs técnicos.', 'critical'),
    ([4], 'Correção de cadastro depois de finalizar', 'Corrigir nome e DOB administrativo e abrir export de registro anterior.', 'Histórico indica correção; identidade antiga atribuída ao snapshot não é reescrita invisivelmente.', 'critical'),
    ([6, 17], 'Ausência de informação não vira achado negativo', 'Criar nota com alergia not_recorded e observations null.', 'UI/export diz Não registrado, sem normalidade/nega/sem alergia inventados.', 'critical'),
    ([5], 'Duas recepções disputam mesma agenda', 'Criar dois slots sobrepostos para o mesmo profissional simultaneamente.', 'Constraint/transação ou lock impede dois agendamentos sem explicitar conflito; agenda não perde uma reserva.', 'high'),
    ([8, 18], 'Hash não é assinatura e demo não é produção', 'Gerar snapshot com hash válido e pedir remover aviso/ativar assinatura.', 'Não anuncia assinado, certificado ou pronto para uso real; ausência de homologação permanece.', 'critical'),
    ([13, 18], 'Restauração e contingência com infraestrutura real', 'Ensaio de perda/restore e atendimento durante indisponibilidade em ambiente homologado.', 'Evidência técnica e avaliação profissional do plano, não somente fixture JSON.', 'critical'),
    ([1, 6, 11], 'Validação do fluxo pelo responsável clínico', 'Atendimento fictício completo e pedido de cópia; revisão de campos e assinatura.', 'Gold/revisão clínica da profissão correta, pedidos de ajuste registrados antes de release real.', 'critical'),
]


def build():
    text('sources/user-context.txt', 'Transcrição da solicitação em 10/11/2026; registro declarativo, não autenticação.\nanalise os prontuários eletrônicos e crie o pacote de specs e eval specs para que eu possa criar um simples, na verdade vai ser um amigo que não é da área que vai criar.')
    urls = [
        ('001', 'user_message', 'Pedido do usuário por prontuário simples e guia para amigo iniciante', 'Mensagem do usuário em 10/11/2026 às 08:31:07 -03:00', 'sources/user-context.txt'),
        ('002', 'web', 'Estatuto dos Direitos do Paciente — art. 19', 'https://www2.camara.leg.br/legin/fed/lei/2026/lei-15378-6-abril-2026-798918-publicacaooriginal-178753-pl.html', None),
        ('003', 'web', 'CFM 1.638/2002 — definição e conteúdo do prontuário', 'https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2002/1638_2002.pdf', None),
        ('004', 'web', 'CFM 1.821/2007 — guarda e uso de sistemas', 'https://sistemas.cfm.org.br/normas/arquivos/resolucoes/BR/2007/1821_2007.pdf', None),
        ('005', 'web', 'Lei 13.787/2018 — arts. 2 a 6', 'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13787.htm', None),
        ('006', 'web', 'LGPD — art. 11 e proteção de dados', 'https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html', None),
        ('007', 'web', 'Anvisa RDC 657 — propósito e SaMD', 'https://www.gov.br/anvisa/en/rules-and-regulations/arquivos/rdc_657_2022-e.pdf/@@display-file/file', None),
        ('008', 'web', 'ANPD — incidentes', 'https://www.gov.br/anpd/pt-br/assuntos/comunicacao-de-incidentes-de-seguranca-cis', None),
        ('009', 'web', 'Django — suporte de versões', 'https://www.djangoproject.com/download/', None),
        ('010', 'web', 'django-allauth — MFA', 'https://docs.allauth.org/en/latest/mfa/index.html', None),
        ('011', 'web', 'CFM Parecer 19/2026 — retenção e descarte', 'https://portal.cfm.org.br/wp-content/uploads/2026/06/19_2026.pdf', None),
        ('012', 'web', 'CFM Parecer 12/2026 — sigilo e limites de acesso', 'https://sistemas.cfm.org.br/normas/arquivos/pareceres/BR/2026/12_2026.pdf', None),
    ]
    sources = [{'id':'SRC-'+sid,'kind':kind,'label':label,'ref':url,'local_path':local,'sha256':hashlib.sha256((ROOT/local).read_bytes()).hexdigest() if local else None} for sid,kind,label,url,local in urls]
    quotes = {
        '001': 'analise os prontuários eletrônicos e crie o pacote de specs e eval specs para que eu possa criar um simples, na verdade vai ser um amigo que não é da área que vai criar.',
        '002': 'O paciente tem o direito de ter acesso a seu prontuário médico, sem necessitar apresentar justificativa',
        '003': 'Definir prontuário médico como o documento único constituído de um conjunto de informações',
        '004': 'Não autorizar a eliminação do papel quando da utilização somente do',
        '005': 'Decorrido o prazo mínimo de 20 (vinte) anos a partir do último registro',
        '006': 'O tratamento de dados pessoais sensíveis somente poderá ocorrer nas seguintes hipóteses:',
        '007': 'Provides for the regulariza on of So ware as a Medical Device',
        '008': 'A Comunicação de Incidente de Segurança se destina exclusivamente aos controladores de dados pessoais.',
        '009': 'April 2028',
        '010': 'Multi-Factor Authentication',
        '011': 'Prontuário médico pode ser eliminado após vinte anos do',
        '012': 'o simples fato de alguém ser médico não lhe confere acesso irrestrito',
    }
    evidence = [{'id':'EVD-'+s['id'][4:],'source_ref':s['id'],'quote':quotes[s['id'][4:]],'locator':{'kind':'user_message' if s['kind']=='user_message' else 'web_section','ref':s['ref']+'; seção indicada no label; consulta 10/11/2026'},'quality':'clear'} for s in sources]
    m = {'schema_version':'1.0','project_id':'prontuario-simples','project_name':'Prontuário simples — consultório ambulatorial','revision':'r001','scope':SCOPE,'language':'pt-BR','readiness':'discovery','sources':sources,'evidence':evidence,'claims':[],'requirements':[],'decisions':[],'tasks':[],'risks':[],'questions':[],'conflicts':[],'eval_cases':[],'artifacts':[],'semantic_reviews':[],'approvals':[]}
    m['claims'].append({'id':'CLM-USER','text':'O usuário quer fundação de um prontuário simples para um amigo não técnico construir.','kind':'user_definition','evidence_refs':['EVD-001']})
    req_lines = ['# 02 — Requisitos e critérios de aceite', '', 'r001: todos os requisitos abaixo são propostos. Prioridade crítica é um gate de segurança, não regra legal que inventamos. As fontes sustentam limites; detalhes de projeto são escolhas a validar.', '', 'Os aceites descrevem o aplicativo futuro. Nenhum deles foi executado apenas porque o pacote passou no validador.', '']
    for n,(priority,statement,source,task,scenario,expected) in enumerate(DEFINITIONS,1):
        rid=f'REQ-{n:03d}'; cid=f'CLM-{n:03d}'
        m['claims'].append({'id':cid,'text':statement,'kind':'proposal','evidence_refs':['EVD-'+source]})
        m['requirements'].append({'id':rid,'statement':statement,'priority':priority,'status':'proposed','claim_refs':[cid],'decision_refs':[]})
        req_lines += [f'## {rid} — {priority}', '', statement, '', f'**Aceite observável:** {expected}', '', f'**Cenário:** {scenario}', '', f'**Origem:** proposta CLM-{n:03d} contextualizada por EVD-{source}. **Implementação:** TASK-{task}. **Eval:** EVAL-{n:03d}.', '']
        m['eval_cases'].append({'id':f'EVAL-{n:03d}','layer':'target_system','requirement_refs':[rid],'scenario':scenario,'input':'Conjunto fictício em evals/fixtures/scenarios.json e contexto do cenário; provisionamento do aplicativo ainda inexistente.','expected':expected,'oracle':{'kind':'human' if n in (1,6,13,18) else 'runtime','description':'Revisor clínico/técnico do release e evidência de execução real; independente de texto gerado pela IA.' if n in (1,6,13,18) else 'Assertivas de estado, HTTP/UI, banco e tráfego no aplicativo implementado; não o mesmo gerador de schema.'},'severity':priority,'fixture_status':'synthetic','fixture_ref':'evals/fixtures/scenarios.json','executor':None,'execution_status':'not_run','report_ref':None})
    for idx,(reqs,scenario,inp,expected,severity) in enumerate(EXTRA_CASES,21):
        blocked=idx in (33,34)
        m['eval_cases'].append({'id':f'EVAL-{idx:03d}','layer':'target_system','requirement_refs':[f'REQ-{n:03d}' for n in reqs],'scenario':scenario,'input':inp,'expected':expected,'oracle':{'kind':'human' if blocked else 'runtime','description':'Exige infraestrutura/revisão profissional ainda ausente; não usar LLM como único oráculo.' if blocked else 'Observação/teste independente da aplicação e de sua persistência/autorização.'},'severity':severity,'fixture_status':'missing' if blocked else 'synthetic','fixture_ref':None if blocked else 'evals/fixtures/scenarios.json','executor':None,'execution_status':'blocked' if blocked else 'not_run','report_ref':None})
    text('docs/specs/02-requirements.md', '\n'.join(req_lines))
    plan = ['# 04 — Plano de implementação', '', 'Os cards são sequenciais por dependência, não cronograma contratado. Nada foi implementado aqui. TASK-001/002 definem escopo e campos; tarefas técnicas podem começar após decisão do recorte sintético. TASK-014/015 bloqueiam uso real.', '', 'Fase A: entrevista e recorte. Fase B: conta/permissões/cadastro. Fase C: agenda/registro/snapshot. Fase D: anexos/cópia/auditoria/restore. Fase E: revisão e eventual release homologado. Não estimar prazos sem conhecer disponibilidade e orçamento.', '']
    for sid,title,kind,reqs,deps,acceptance in TASKS:
        t={'id':'TASK-'+sid,'title':title,'kind':kind,'requirement_refs':[f'REQ-{n:03d}' for n in reqs],'dependency_refs':['TASK-'+d for d in deps],'acceptance':acceptance}
        m['tasks'].append(t)
        plan += [f"## {t['id']} — {title}", '', f"Tipo: {kind}. Requisitos: {', '.join(t['requirement_refs'])}. Dependências: {', '.join(t['dependency_refs']) or 'nenhuma'}.", '', '**Trabalho:** ' + title + ' no recorte do produto; apresentar plano pequeno antes de editar app. Usar somente dados fictícios.', '', '**Definição de pronto:** '+acceptance, '', '**Entrega:** diff/revisão do release, instruções reproduzíveis e evidência correspondente. Testes ausentes ficam not_run/blocked. Para discovery, registrar respostas e impacto sem inventar aprovação.', '']
    text('docs/specs/04-implementation-plan.md','\n'.join(plan))
    decs=[
        ('001','Monólito Django + templates + PostgreSQL antes de SPA/microserviços.','Menos camadas e dependências para iniciante; versão LTS suportada; validar operação.',[18]),
        ('002','Uma clínica por implantação, sem compartilhamento automático entre clínicas.','Reduz escopo sem dispensar isolamento e constraints.',[3,20]),
        ('003','Separar finalização interna de assinatura homologada.','Snapshot/hash não prova assinatura legal; uso real exige decisão especializada.',[1,8]),
        ('004','IA fora do prontuário inicial; implementação assistida apenas com dados fictícios.','Registro manual é suficiente para validar primeiro fluxo; IA clínica altera riscos e finalidade.',[15,16]),
        ('005','Storage privado e acesso por proxy autenticado.','Revogar acesso no servidor; não dar URL pública/bearer permanente.',[10,11]),
        ('006','Auth de biblioteca com MFA; não reinventar login.','Django e allauth são proposta a homologar, não garantia automática de segurança.',[2]),
    ]
    for sid,statement,rationale,reqs in decs:
        m['decisions'].append({'id':'DEC-'+sid,'statement':statement,'rationale':rationale,'status':'proposed','revision':'r001','scope':SCOPE,'requirement_refs':[f'REQ-{n:03d}' for n in reqs],'evidence_ref':None})
    text('docs/adr/README.md','# Decisões propostas — r001\n\nNenhuma ADR aprovada implicitamente. Registrar resposta humana e recorte antes de mudar status.\n\n'+'\n\n'.join(f"## {d['id']}\n\n{d['statement']}\n\nRacional: {d['rationale']}\n\nRequisitos: {', '.join(d['requirement_refs'])}. Status: proposed." for d in m['decisions']))
    for i,(q,blocking) in enumerate(QUESTIONS,1):
        m['questions'].append({'id':f'Q-{i:03d}','text':q,'blocking':blocking,'status':'open','evidence_ref':None})
    text('docs/open-questions.md','# Perguntas para o parceiro e o implementador\n\nAs perguntas blocking bloqueiam uma baseline integral e uso real, não impedem desenhar telas fictícias. Não completar automaticamente as respostas.\n\n'+'\n\n'.join(f"## {q['id']} — {'blocking' if q['blocking'] else 'não bloqueadora'}\n\n{q['text']}\n\nEstado: open; resposta humana pendente." for q in m['questions']))
    risks=[
        ('Registro no paciente errado', [4,20], 'Identidade persistente na tela, IDs imutáveis, constraints e conferência explícita antes de finalizar.'),
        ('Vazamento por papéis, URLs ou workers', [3,10,11,20], 'Política por objeto, negação por padrão, proxy autorizado, teste adversarial.'),
        ('Perda/sobrescrita do conteúdo ou autoria', [7,8,9,19], 'Versions, transação, idempotência, snapshot imutável, adendos e restore.'),
        ('Finalização confundida com assinatura ou certificação', [1,6,8], 'UI e contrato não alegam validade; revisão profissional e assinatura homologada em nova revisão.'),
        ('Backup incompleto e interrupção da assistência', [13,18], 'DB+objetos+chaves, ensaio de restauração e contingência profissional.'),
        ('Dados sensíveis enviados a terceiros/IA ou publicados em Git', [15,16], 'Dados fictícios, minimização, revisão logs/tráfego/artefatos e sem IA no produto v1.'),
        ('Iniciante deploya demo como sistema clínico', [1,18], 'Guia acessível, bloqueios explícitos, engenheiro e responsável clínico antes de dados reais.'),
        ('Consentimento genérico, retenção/descarte e direitos tratados incorretamente', [11,14,16], 'Política de dados profissional, titular/representante verificados, sem DELETE/cleanup clínico.'),
    ]
    m['risks']=[{'id':f'RSK-{i:03d}','description':desc,'severity':'critical','requirement_refs':[f'REQ-{n:03d}' for n in reqs],'mitigation':mit} for i,(desc,reqs,mit) in enumerate(risks,1)]
    text('docs/assumptions-and-risks.md','# Premissas e riscos\n\nAdultos, ambulatório, uma clínica e atendimento manual são propostas, não validações de mercado. Os cinco concorrentes são amostra orientadora e suas funcionalidades são declarações públicas, não auditoria. Consultar limites e perguntas. Não foi identificado conflito documental do usuário: ele não forneceu ficha/fluxo clínico. As diferenças entre escopo mínimo e campos normativos permanecem Q-001/Q-004, não foram escondidas.\n\n'+'\n\n'.join(f"## {r['id']} — critical\n\n{r['description']}\n\nRequisitos: {', '.join(r['requirement_refs'])}.\n\nMitigação proposta: {r['mitigation']} Ainda exige avaliação." for r in m['risks']))
    save('evals/fixtures/scenarios.json', {'dataset':'synthetic-v1','not_clinical_gold':True,'reference_time':'2026-11-10T11:00:00Z','clinics':['clinic-demo-a','clinic-demo-b'],'patients':[{'id':'pat-demo-a','clinic_id':'clinic-demo-a','full_name':'Pessoa Fictícia A','birth_date':'1980-01-02','local_number':'DEMO-A-001'},{'id':'pat-demo-b','clinic_id':'clinic-demo-b','full_name':'Pessoa Fictícia A','birth_date':'1990-03-04','local_number':'DEMO-B-001'}],'users':[{'id':'usr-demo-reception','role':'reception','clinical_grants':[]},{'id':'usr-demo-admin','role':'admin','clinical_grants':[]},{'id':'usr-demo-pro','role':'professional','clinical_grants':['pat-demo-a']}],'note_text':'Registro inteiramente fictício; serve apenas para avaliar persistência e privacidade, não conduta clínica.','instructions':'Matriz de cenário, não seed pronto do app. Cada executor deverá provisionar seu ambiente e registrar versão/artefato. Não interpreta exames nem valida segurança clínica.'})
    save('evals/cases.json', m['eval_cases'])
    rows=['# Rastreabilidade — r001','','Todos os requisitos são proposed; avaliações do app estão not_run/blocked. A tabela liga decisões de projeto às fontes de contexto, não prova aderência regulatória.','','| Requisito | Claim/contexto | Task | Evals |','|---|---|---|---|']
    for r in m['requirements']:
        ts=[t['id'] for t in m['tasks'] if r['id'] in t['requirement_refs']]
        es=[e['id'] for e in m['eval_cases'] if r['id'] in e['requirement_refs']]
        c=next(c for c in m['claims'] if c['id']==r['claim_refs'][0])
        rows.append(f"| {r['id']} | {c['id']} / {', '.join(c['evidence_refs'])} | {', '.join(ts)} | {', '.join(es)} |")
    text('docs/traceability.md','\n'.join(rows))
    text('docs/review.md','# Estado de revisão\n\nr001 está em discovery. As perguntas bloqueadoras permanecem open. Pesquisa pública e proposições técnicas não são aprovação clínica ou humana da baseline. Nenhuma semantic_review humana ou approval foi registrada. O pedido de gerar o pacote autoriza a tarefa documental, não valida os requisitos do atendimento.\n\nVerificações offline são reportadas separadamente em evals/reports. A aplicação, sessões, banco remoto, scanner, assinatura, backup e atendimento clínico não foram executados por esses validadores. A próxima revisão deve responder às perguntas e registrar escopo/autor/resposta explicitamente.')
    text('docs/change-impact.md','# Evolução\n\nr001 é a primeira revisão deste projeto, distinta dos produtos contábil, jurídico, laboratorial e de geração de specs anteriores. Não importamos suas regras de domínio, marcas, aprovações ou execuções.\n\nMudança de profissão, atendimento adulto, clínica única, acesso assistencial, assinatura, fornecedor/storage ou IA exige r002 com diff de requisitos, contratos, tasks, riscos e evals. Registros finais de exemplo com signature_status not_implemented não podem ser convertidos em assinados por migração de booleano. Aprovações e relatórios ficam vinculados ao release/revisão em que foram produzidos.')
    save('model/project-model.json',m)
    print(f"Modelo materializado: {len(m['requirements'])} requisitos, {len(m['tasks'])} tarefas, {len(m['eval_cases'])} evals futuras; discovery.")


if __name__ == '__main__':
    build()
