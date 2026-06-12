# Capítulo 11 — Funções e testes

Este capítulo cobre boas práticas para funções e testes.

## Funções
- Devem ser pequenas e fazer uma única coisa.
- Separam lógica do programa e facilitam reuso.

## test_
- Funções de teste geralmente começam com `test_`.
- Arquivos de teste também começam com `test_`.

## assert
- `assert` verifica resultados esperados.
- Lança `AssertionError` se a condição falhar.

## pytest
- Framework popular para testes em Python.
- Detecta automaticamente testes em arquivos nomeados corretamente.

## Casos de teste
- Teste entradas válidas e inválidas.
- Verifique retornos e exceções.
