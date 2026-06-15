# Resumo Teórico — Filtros Digitais

Os filtros digitais são sistemas utilizados para modificar seletivamente componentes espectrais de sinais discretos. Sua principal função consiste em atenuar ruídos, remover interferências ou destacar frequências de interesse em sinais digitais.

Os filtros digitais podem ser classificados em duas categorias principais: FIR (Finite Impulse Response) e IIR (Infinite Impulse Response).

## Filtros FIR

Os filtros FIR possuem resposta ao impulso finita. Isso significa que, após determinado intervalo de tempo, a saída causada por um impulso desaparece completamente.

As principais características dos filtros FIR são:

- estabilidade inerente;
- possibilidade de fase linear;
- implementação simples;
- maior custo computacional em algumas aplicações.

Filtros FIR são muito utilizados em aplicações que exigem preservação da forma do sinal, como processamento de áudio e imagens.

## Filtros IIR

Os filtros IIR possuem resposta ao impulso infinita devido à presença de realimentação.

Principais características:

- maior seletividade;
- menor ordem necessária;
- menor custo computacional;
- possibilidade de instabilidade;
- fase não linear.

Filtros IIR são bastante utilizados em sistemas embarcados e aplicações em tempo real.

## Resposta em Frequência

A resposta em frequência descreve como o filtro modifica cada componente espectral presente no sinal.

Filtros podem ser classificados em:

- passa-baixa;
- passa-alta;
- passa-faixa;
- rejeita-faixa.

## Resposta de Fase

A resposta de fase indica o deslocamento aplicado às componentes espectrais do sinal.

Filtros com fase linear preservam melhor a forma temporal dos sinais.

## Atraso de Grupo

O atraso de grupo representa o atraso introduzido pelo filtro em diferentes frequências.

Esse parâmetro é importante em:

- telecomunicações;
- transmissão digital;
- processamento de áudio.

## Estabilidade

A estabilidade de filtros digitais depende da localização dos polos no plano-z.

Para filtros IIR estáveis:

- todos os polos devem permanecer dentro do círculo unitário.

## Aplicações Práticas

Filtros digitais são utilizados em:

- redução de ruído;
- sensores industriais;
- telecomunicações;
- processamento de áudio;
- monitoramento de vibração;
- TinyML;
- sistemas embarcados.
