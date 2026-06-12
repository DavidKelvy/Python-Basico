# Capítulo 10 — Arquivos e exceções

Conceitos encontrados:

- **abrir arquivos**: `open(path, mode)` com modos `'r'`, `'w'`, `'a'`, `'r+'`.
- **ler arquivos**: `.read()`, `.readline()`, `.readlines()`.
- **escrever arquivos**: `.write()` e `with open(...) as f:` para gerenciar contexto.
- **context manager (`with`)**: garante fechamento automático do arquivo.
- **exceções**: `try/except/else/finally` para tratar erros (ex.: `FileNotFoundError`, `ValueError`, `ZeroDivisionError`).
- **json**: `json.load()` e `json.dump()` para armazenar e recuperar estruturas em arquivos `.json`.
- **contagem e processamento de texto**: ler arquivos grandes e processar linhas (ex.: contagem de palavras).

Tratamento de arquivos e exceções torna o código mais robusto.
