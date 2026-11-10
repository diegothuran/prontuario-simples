# Exemplos sintéticos

Sete examples acompanham os schemas v0.1. Pessoa Fictícia A e IDs demo não representam ninguém. Texto clínico é placeholder de teste de salvamento e não é diagnóstico, receita, anamnese adequada ou orientação de atendimento.

Data de referência dos contratos: 10/11/2026, explicitada no checker. Datas não devem avançar sozinhas para esconder falha. A matriz de eval usa outra referência de cenário para planejamento; não é relógio operacional. Os exemplos são fixtures de forma/vínculo; não seed pronto de banco Django nem gold clínico.

O record-snapshot está finalized apenas para testar a estrutura de fechamento; signature_status permanece not_implemented. Attachment clean no exemplo contém metadados declarados de scan fictício: o checker não executa antivírus. Export ready é um estado fictício e não contém pacote clínico realmente gerado. Não apontar para pacientes ou buckets reais para “completar” a fixture.

Novos exemplos devem permanecer sintéticos, com enunciado e resultado esperado de oráculo independente, e atualizar contratos/modelo em revisão explícita se alterarem regra material.
