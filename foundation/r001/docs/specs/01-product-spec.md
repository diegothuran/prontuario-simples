# 01 — Produto: prontuário simples

Revisão r001, proposta em discovery, Brasil, 10/11/2026. Nome descritivo, não marca escolhida. O usuário pediu análise e fundação para um amigo não técnico criar o sistema. Não foram definidos clínica, profissão, especialidade, orçamento, hospedagem ou autorização de uso real.

## Objetivo

Permitir que uma equipe pequena encontre o paciente correto, organize uma consulta presencial e registre manualmente o que aconteceu, preservando histórico, autoria e privacidade. O primeiro sucesso é uma jornada fictícia completa e compreensível, não centenas de funções.

## Público e hipótese inicial

Consultório ambulatorial, uma clínica por implantação, poucos usuários e atendimento adulto no protótipo. Essa hipótese reduz complexidade, mas precisa ser confirmada. Não presumir que todo profissional seja médico ou que as regras do CFM se apliquem a todas as profissões.

Recepção cuida de cadastro e agenda; profissional habilitado registra o atendimento; administrador gerencia contas e operação. Um administrador que também atende recebe um vínculo profissional separado. Responsável clínico e revisor técnico são pessoas necessárias antes de uso real; não são papéis que a IA pode assumir.

## Jornada de referência

1. Usuário autorizado entra com conta individual.
2. Recepção busca paciente por nome/data de nascimento/número local e verifica identidade; homônimos não são mesclados automaticamente.
3. Recepção agenda ou registra chegada. Atendimento sem agendamento também é possível.
4. Profissional com vínculo assistencial explícito abre o paciente, revisa histórico e cria um atendimento.
5. Profissional escreve observações em campos organizados, salva rascunho e recebe confirmação do servidor.
6. Profissional revê a identidade, conteúdo e versão; fecha um snapshot imutável na aplicação.
7. Correções posteriores são novos adendos identificados; o original permanece acessível.
8. Cópia é preparada e entregue ao titular ou representante após verificação de identidade/autoridade. Não é um link público.

## Dentro da primeira entrega de desenvolvimento

Cadastro básico e pesquisa; agenda simples; vínculo profissional-paciente; registro textual de atendimento e evolução; histórico cronológico; anexos privados em quarentena; exportação controlada; trilha de acesso; contas individuais e MFA; backup e ensaio de restauração. Contratos e testes incluem versões, falhas de rede e tentativas de acesso indevido.

## Fora da v1

IA clínica ou administrativa sobre dados reais, receitas/atestados/guias, interação medicamentosa, cálculo de dose, diagnóstico automatizado, telemedicina, cobrança, financeiro, convênios/TISS, RNDS/SUS, laboratório, hospital/internação, aplicativo nativo, integração com equipamentos, compartilhamento automático entre clínicas e importação em massa de prontuários reais. Não construir cadastro genérico de formulários ou marketplace antes do fluxo principal.

Menores, tutores, situações de incapacidade e especialidades com sigilo particular não entram na demo adulta; terão desenho próprio antes de expansão. Isso não autoriza uma aplicação produtiva a negar direitos: a clínica deve confirmar que o público real cabe no recorte.

## O que a simplicidade não elimina

Acesso clínico controlado, segurança, autoria, preservação, continuidade e direito de cópia fazem parte do produto mínimo. Não delegar esses assuntos apenas ao cliente nem adiá-los sob o argumento de que haverá poucos pacientes.

## Dois portões distintos

**Demonstração sintética:** sem pacientes reais, sem credenciais compartilhadas e sem alegar assinatura digital. O fechamento `finalized` é uma ação da aplicação e a assinatura permanece `not_implemented`.

**Uso assistencial real:** exige confirmação da profissão e especialidade, formulário clínico revisado, assinatura/preservação juridicamente adequada, políticas de dados, revisão de engenharia, restore testado, suporte e validação formal do release. O pacote não libera esse portão.

## Valor e hipóteses de diferenciação

O benchmark orienta capacidades, não clones. Diferenciais propostos para testar com um consultório são fluxo curto, clareza sobre salvamento, exportação compreensível e facilidade de operação em conexão instável. Ainda não há pesquisa com clientes ou prova de lacuna de mercado. Não anunciar redução de erros clínicos ou tempo de atendimento sem estudo.

## Critérios de sucesso da descoberta

Parceiro explica uma consulta real sem usar dados de paciente; define campos e permissões; amigo consegue descrever a diferença entre salvar, finalizar e assinar; equipe concorda com as funções excluídas. Métricas do software só serão medidas quando existir aplicação. Consulte [perguntas abertas](../open-questions.md) e [limites de saúde](../regulatory-and-clinical-boundaries.md).
