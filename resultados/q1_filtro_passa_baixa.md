# Resultado — Questão 1

Foi gerado um sinal composto por duas senoides:

- 50 Hz
- 250 Hz

Em seguida, foi aplicado um filtro FIR passa-baixa com frequência de corte de 100 Hz.

## Resultado Observado

Após a filtragem:

- a componente de 50 Hz permaneceu praticamente intacta;
- a componente de 250 Hz foi fortemente atenuada.

## Interpretação

O filtro passa-baixa permitiu apenas a passagem das frequências abaixo da frequência de corte estabelecida.

Isso demonstra o comportamento seletivo dos filtros digitais no domínio da frequência.

## Conclusão

O filtro FIR apresentou bom desempenho na remoção da componente de alta frequência, preservando o sinal desejado.
