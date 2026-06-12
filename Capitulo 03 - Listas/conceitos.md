# Capítulo 03 — Listas

Este capítulo mostra listas e como operar coleções ordenadas.

## O que é uma lista?
- Uma lista é uma coleção ordenada e mutável.
- Sintaxe: `[1, 2, 3]`.

## Acessar elementos
- `lista[0]` acessa o primeiro elemento.
- `lista[-1]` acessa o último elemento.
- `lista[1:3]` retorna um pedaço (slice).

## Adicionar e remover
- `.append(item)` adiciona ao final.
- `.insert(index, item)` insere em posição específica.
- `.remove(item)` remove a primeira ocorrência do item.
- `.pop(index)` remove e retorna o item.

## Ordenação e cópias
- `.sort()` ordena a lista no lugar.
- `sorted(lista)` cria uma nova lista ordenada.
- `lista[:]` ou `list(lista)` criam cópias.

## Laços e listas
- `for item in lista:` percorre cada elemento.
- `enumerate(lista)` retorna índice e valor.

## Compreensões de lista
- Criam listas de forma concisa.
- Exemplo: `[x**2 for x in range(5)]`.
