# Prontuário Simples

Fundação aberta de **specs e eval specs** para construir um prontuário ambulatorial brasileiro simples, com desenvolvimento assistido por IA e dados exclusivamente fictícios nesta etapa.

> **Estado atual: planejamento em discovery. Não há aplicativo clínico neste repositório.** Não é prontuário certificado, não garante conformidade e não está liberado para atendimento de pacientes reais. A licença de código/documentação não substitui revisão clínica, segurança, assinatura adequada ou operação responsável.

## Começar após o clone

```bash
git clone https://github.com/diegothuran/prontuario-simples.git
cd prontuario-simples
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python scripts/check_repository.py
```

Leia [START-HERE.md](START-HERE.md). Esse comando **testa a fundação**, não inicia prontuário, banco, serviço cloud ou atendimento.

## Primeiro produto proposto

Uma clínica por implantação, atendimento adulto ambulatorial como hipótese a validar, poucos usuários com contas individuais. Cadastro/busca → agenda → atendimento manual → rascunho versionado → snapshot fechado → histórico/adendos → anexos privados/cópia autorizada.

Stack recomendada: Django LTS, templates server-side e PostgreSQL. Login/MFA de biblioteca a homologar; storage privado. Evitar SPA, microserviços e integrações no começo. IA auxilia a programar com dados fictícios, não diagnostica, prescreve ou processa dados clínicos neste produto inicial.

Fora da v1: IA clínica/transcrição, receitas/atestados, telemedicina, hospital/internação, financeiro/convênios e integrações. O mínimo não dispensa identificação correta, permissões por objeto, preservação, acesso/cópia, backup restaurável e apoio de profissionais adequados.

## O que já existe

- Pesquisa pública de iClinic, Feegow, Amplimed, Ninsaúde Clinic e HiDoctor; não auditoria de seus produtos.
- Cinco specs principais e **20 requisitos**, **15 tarefas** e **34 cenários de avaliação do aplicativo futuro**.
- Domínio, sete contratos JSON com exemplos fictícios, fluxos de telas, limites regulatórios, perguntas e riscos.
- **23 testes locais de estrutura/contratos** aprovados na preparação da r001; zero casos de produto executados.
- Snapshot `foundation/r001/` com manifest e hashes; CI de checks documentais/contratos, sem pacientes, banco ou segredos.

Os 34 casos-alvo da r001 permanecem 32 `not_run` e 2 `blocked`. Teste verde do pacote **não é** aprovação para uso clínico. Snapshot finalizado/hash não equivale a assinatura digital juridicamente suficiente.

## Organização

```text
foundation/r001/      # specs, evals, schemas, fixtures e manifest congelados
scripts/             # check da distribuição/repositório
.github/workflows/   # CI offline da fundação, sem deploy
README.md
START-HERE.md
AGENTS.md
CLAUDE.md
CONTRIBUTING.md
SECURITY.md
LICENSE              # MIT
```

Arquivos de aplicação ainda não existem. Eles poderão ser criados em tarefas autorizadas após definir o recorte sintético. Não regenerar/editar o snapshot para encaixar o código: mudança material pede revisão r002 e rastreabilidade.

## Leitura guiada

- [Guia da fundação](foundation/r001/docs/START-HERE.md)
- [Benchmark](foundation/r001/docs/benchmark-and-scope.md)
- [Produto](foundation/r001/docs/specs/01-product-spec.md) e [requisitos](foundation/r001/docs/specs/02-requirements.md)
- [Desenho](foundation/r001/docs/specs/03-system-design.md) e [backlog](foundation/r001/docs/specs/04-implementation-plan.md)
- [Telas/estados](foundation/r001/docs/ux-and-screen-contracts.md)
- [Perguntas bloqueadoras](foundation/r001/docs/open-questions.md) e [limites clínicos](foundation/r001/docs/regulatory-and-clinical-boundaries.md)
- [Eval specs](foundation/r001/evals/eval-spec.md) e [verificação local registrada](foundation/r001/docs/VERIFICATION.md)
- [Desenvolvimento](docs/DEVELOPMENT.md) e [contribuição](CONTRIBUTING.md)

## Trabalho com IA

Use [AGENTS.md](AGENTS.md)/[CLAUDE.md](CLAUDE.md). Peça uma tarefa pequena, confira diff e testes, não complete dúvidas clínicas com suposição. Primeiro: TASK-001/002, profissão/especialidade e modelo de consulta com parceiro da área. Depois: tarefa técnica sintética autorizada. Antes do primeiro paciente real: revisão profissional/técnica, assinatura/preservação, privacidade, restore, suporte e aceite do release.

## Projeto aberto

Distribuído sob [licença MIT](LICENSE). As fontes públicas são citadas para referência; seus direitos e termos não são substituídos pela licença deste projeto. Não há código proprietário dos concorrentes nem telas copiadas. Contribuições devem manter as fronteiras de saúde e segurança e usar somente fixtures fictícias.

Não envie prontuários, fotos/exames de pacientes, tokens, certificados ou dumps em issues, PRs ou prompts. Consulte [SECURITY.md](SECURITY.md) para relatos de vulnerabilidade sem exposição de informações sensíveis.
