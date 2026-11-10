# Instruções de agentes

Este projeto é a fundação r001 de um prontuário simples, proposta em discovery. Não é um sistema de atendimento já implementado. Leia README, docs/START-HERE.md, os cinco anchors e evals/eval-spec.md antes de agir.

1. Trabalhe uma tarefa pequena por vez; explique para iniciante e teste o alcance correto.
2. Proposta não é aprovação. Perguntas de profissão, campos, assinatura, dados e operação exigem pessoas adequadas. Registre respostas e impacto; não invente clinical gold.
3. Use somente dados fictícios. Não coloque pacientes, exames reais, dumps, chaves ou tokens em prompts/Git/screenshots/logs.
4. Sem IA clínica, diagnóstico, dose, receita, atestado, telemedicina, integrações ou microserviços na v1.
5. Admin/recepção não herdam acesso clínico. Autorização é por objeto e vínculo assistencial, no servidor. Campos autoritativos nunca vêm do cliente.
6. Snapshot finalized não equivale a assinado digitalmente. Não alterar `not_implemented` por booleano sem nova revisão/provedor validado.
7. Nunca alterar/excluir original finalizado; adendo é novo registro atribuído. Preservar identidade, datas e versões.
8. `python scripts/check_foundation.py` testa o pacote. Não declarar validação clínica/conformidade ou mudar eval target para passed por esse resultado.
9. Não publicar dados, fazer deploy/merge ou usar clínica real por inferência. Ação externa requer autorização própria.
10. Mudança material gera r002 com rastreabilidade; não reutilizar aprovação/relatório antigo como evidência do release novo.
