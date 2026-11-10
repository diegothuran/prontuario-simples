# Contratos de dados — proposta 0.1

Os JSON Schemas desta pasta descrevem formatos e algumas invariantes offline. Não criam um backend nem validam profissão, identidade, sessão, vínculo assistencial, malware ou assinatura. O schema do ProjectModel é outro contrato: rastreia a fundação, não o prontuário.

## Fronteira de autoridade

| Contrato | Papel | Autoridade |
|---|---|---|
| patient | Snapshot administrativo mínimo da demo | ID, clínica, número local, versão/status são atribuídos pelo servidor |
| draft-command | Edição do texto de nota existente, com encounter_id e expected_version | Usuário só propõe texto; servidor verifica encounter, autoria, vínculo e versão |
| finalize-command | Fechar versão conhecida com chave idempotente | Não aceita conteúdo novo, author_id, clinic_id, data ou signed |
| record-snapshot | Resultado fechado da aplicação | Servidor atribui identidade, autor profissional, datas, versão/hash; assinatura segue não implementada |
| addendum-command | Solicitar adendo, motivo e texto | Autoria e contexto derivam da sessão; snapshot original não se modifica |
| attachment | Metadados controlados do anexo | Storage key, bytes/hash, resultado e versão de scan são calculados/validados por infraestrutura |
| export-job | Estado de job de cópia | Copy request verificado, fontes e status são controlados; não permite baixar por conhecer o ID |

`additionalProperties: false` nos comandos rejeita campos inesperados; não confiar em descartar silenciosamente papel/autoria e continuar. Validar JSON e formulário de UI com a mesma regra. `expected_version` é inteiro >=1; 409 exige reconciliação, não retentativa cega da edição. Chave idempotente é opaca e escopada por clínica+ator+operação; payload divergente na mesma chave retorna conflito.

## Conteúdo clínico de demonstração

Os campos chief_complaint/history/observations/assessment/plan são texto manual ou null. Nenhum null implica achado ausente. Na aplicação não há geração clínica. A ficha real, regras de completude e campos normativos dependem da profissão e do modelo homologado; a regra offline de haver algum texto não valida suficiência clínica. Anexo não substitui anamnese automaticamente.

`allergy_status: not_recorded` não equivale a `none_reported`. `known` exige detalhe textual como registro humano; não valida alergia ou prevê interação. Essa definição é proposta de armazenamento, não protocolo médico. Origem e datas no app devem acompanhar o registro.

## Hash e datas

`content-json-v1` usa JSON UTF-8, chaves ordenadas, `ensure_ascii=False`, separadores sem espaços e sem normalização implícita do texto. A implementação pode usar a mesma referência de serialização Python do pacote; se usar outro runtime precisa testes de compatibilidade e versão de canonicalização. Não confundir com padrão universal RFC de assinatura.

O hash do conteúdo detecta divergência dos bytes canonicalizados, mas não protege sozinho metadados/autoria nem impede um administrador de recalcular o hash. Preservação de snapshot completo, conta DB, auditoria segregada, backup e assinatura adequada são controles distintos. Horários têm timezone explícito; data de nascimento é date sem timezone. A UI mostra horário local; servidor persiste UTC. Registros retrospectivos preservam hora de gravação e motivo.

## O que faltará antes do uso real

Ficha administrativa e clínica da profissão, representante e direitos aplicáveis, tabelas/migrations, permissões por objeto, contrato/provedor de assinatura, storage/scanner, geração de cópia e testes reais. Os schemas não bastam para certificação ou apagar papel. Nenhum modelo de receita/atestado foi incluído.

Exemplos são fictícios e têm identificação explícita de demo. Consulte [domínio](domain-model.md), [desenho](specs/03-system-design.md) e [limites](regulatory-and-clinical-boundaries.md).
