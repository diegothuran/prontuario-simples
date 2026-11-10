# Instruções do repositório

Este é o repositório aberto da fundação de Prontuário Simples; não existe app clínico pronto. Use só dados fictícios. Leia README/START-HERE e a documentação requerida da tarefa.

- `foundation/r001/` é snapshot congelado com manifest. Não editar nem atualizar hashes para mascarar mudanças. r002 para alteração material; código futuro separado da fundação.
- Requisitos/decisões são propostas em discovery. Quem decide profissão, campos, assinatura, acesso e release real são responsáveis apropriados, não a IA.
- Trabalhar uma tarefa pequena autorizada por vez; explicar para iniciante; mostrar diff, testes e limitações.
- Nada de prontuários/exames reais, segredos, dumps, chaves ou screenshots identificáveis em Git/prompts/issues/logs.
- Sem IA clínica, doses, receitas/atestados, telemedicina, integrações ou microserviços na v1.
- Admin/recepção não herdam acesso clínico. Policies por objeto e vínculo assistencial são server-side. Snapshot/hash não é assinatura homologada.
- `python scripts/check_repository.py` testa repositório/contratos offline, não app, scanner, autorização HTTP, restore ou conformidade.
- Não marcar target eval passed por executar check de schema. Caso exige release/ambiente/executor/evidência e limitações.
- Não publicar/implantar/mesclar/excluir ou usar pacientes reais por inferência. A autorização da contribuição não libera produção.
- Use bibliotecas suportadas e revisão de engenheiro experiente para controles críticos. Licença MIT não certifica software de saúde.
