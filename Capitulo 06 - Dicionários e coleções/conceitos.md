# Capítulo 06 — Dicionários e coleções

Este capítulo explica estruturas para armazenar pares e coleções.

## Dicionário
- Dicionários ligam chaves a valores.
- Sintaxe: `{'nome': 'Ana', 'idade': 30}`.

## Acesso e métodos
- `dict['chave']` obtém o valor.
- `dict.get('chave', default)` evita erro se a chave não existir.
- `.keys()`, `.values()`, `.items()` retornam chaves, valores e pares.

## Alterar e remover
- `dict['nova'] = valor` adiciona ou atualiza.
- `.pop('chave')` remove e retorna o valor.
- `.update(other)` combina dicionários.

## Tuplas
- Tuplas são sequências imutáveis: `(1, 2, 3)`.
- Não podem ser alteradas depois de criadas.

## Conjuntos
- `set` guarda elementos únicos.
- Operações como união (`|`), interseção (`&`) e diferença (`-`).

## Coleções aninhadas
- Dicionários podem conter listas e outros dicionários.
