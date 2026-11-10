# Rubricas de revisão

Use pass/fail/blocked com evidência, nunca nota subjetiva para compensar falha crítica. Revisor independente do gerador da solução sempre que possível. Revisão profissional não pode ser substituída por texto persuasivo da IA.

## Fidelidade do registro

Pass: identidade, texto, autor, momento assistencial/gravação e sequência snapshot/adendos conferem com fixture autorizada; alterações explicitadas. Fail: sumiu conteúdo, mudou paciente/autor ou acrescentou informação não registrada. Blocked: falta campo/gold/revisor da profissão para julgar suficiência clínica. O teste textual de um JSON não certifica validade do prontuário.

## Privacidade e autorização

Pass: matriz negativa/positiva provada em UI, HTTP, banco e downloads/workers. Fail crítico: conteúdo clínico recebido por recepção/admin não clínico/profissional sem vínculo/terceiro; grant forjado; dados em logs/terceiros. Blocked: apenas botão oculto ou mock sem backend. Não pedir ao iniciante para testar ataque em produção.

## Salvamento e integridade

Pass: commit confirmado, 409 e corrida real em PostgreSQL, idempotência consistente, original imutável e adendo atribuído. Fail crítico: falso Salvo, perda silenciosa, escrita em finalized, duplicata de finalização. Blocked: fixture estática sem concorrência executada. Hash recalculado pelo servidor não é prova autônoma de assinatura.

## Arquivos e cópia

Pass: bytes privados, scan e política por objeto verificadas; export compatível com fontes e direitos/identidade do titular; indicadores de anexos indisponíveis. Fail crítico: objeto público/scan bypass, documento de outro paciente, terceiro sem poderes, recusa de cópia por ausência de justificativa clínica. Blocked: scanner real ou entrega/política não definido. Não usar “gera PDF” como evidência de prontuário digital válido.

## Operação

Pass: restore completo observado com tempo/perda, responsabilidades, chaves e suporte; plano de indisponibilidade aceito pela clínica. Fail crítico: backup que restaura só metadados, chaves perdidas, release sem revisão, produção compartilhada com demo. Blocked: script nunca exercitado ou sem responsáveis. Custo/uptime anunciado por fornecedor não comprova operação do nosso produto.

## Usabilidade

Pass: usuário autorizado conclui jornada sem trocar de paciente; labels/foco/teclado, celular, nomes de preferência, estado Não registrado, erro/rede/timeout compreensíveis. Fail: foco perdido, status ambíguo ou erro que causa troca/perda; classificar crítico se cria risco material, não apenas estética. Blocked: apenas screenshot bonito sem tarefas/estados. Contraste e leitor de tela precisam verificação real.
