# Capítulo 02 — Strings e variáveis

Este capítulo explica texto e variáveis em Python.

## Strings
- Strings são valores de texto, criadas com aspas simples ou duplas.
- Exemplo: `'texto'` ou `"texto"`.
- Use `
` para nova linha e `	` para tabulação.

## Variáveis
- Variáveis guardam dados usando `nome = valor`.
- Use `snake_case` para nomes claros.
- Exemplo: `first_name = 'Ada'`.

## Métodos de string
- `.title()` capitaliza cada palavra.
- `.upper()` converte tudo para maiúsculas.
- `.lower()` converte tudo para minúsculas.
- `.replace(old, new)` substitui texto.
- `.strip()` remove espaços no começo e no fim.
- `.startswith(prefix)` verifica início da string.
- `.split(sep)` divide a string.
- `sep.join(lista)` junta elementos em uma string.

## Formatação
- F-strings (`f'...'`) inserem variáveis dentro de texto.
- Preferidas sobre concatenação com `+`.

## Tamanho e representação
- `len(string)` retorna o número de caracteres.
- `repr(string)` mostra a representação literal.

## Boas práticas
- Não use nomes de funções built-in como `list` ou `str`.
- Mantenha variáveis e mensagens descritivas.
