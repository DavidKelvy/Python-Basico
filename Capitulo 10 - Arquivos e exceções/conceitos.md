# Capítulo 10 — Arquivos e exceções

Este capítulo explica leitura/escrita de arquivos e tratamento de erros.

## Abrir arquivo
- `open('arquivo.txt', 'r')` para leitura.
- `open('arquivo.txt', 'w')` para escrita.
- `open('arquivo.txt', 'a')` para anexar.

## with
- O context manager `with` fecha o arquivo automaticamente.
- Reduz risco de arquivos abertos e erros.

## Leitura
- `.read()` lê todo o conteúdo.
- `.readline()` lê uma linha.
- `.readlines()` lê todas as linhas como lista.

## Escrita
- `.write(texto)` grava texto.
- `.writelines(lista)` grava várias linhas.

## JSON
- `json.load()` lê de arquivo JSON.
- `json.dump()` grava objetos Python em JSON.

## Exceções
- `try` executa o código que pode falhar.
- `except` captura erros específicos.
- `finally` executa sempre, mesmo após erro.
