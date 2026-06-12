# Capítulo 16 — Dados e CSV

Este capítulo ensina a trabalhar com dados tabulares.

## CSV
- Arquivo CSV contém valores separados por vírgula.
- Cada linha representa um registro.

## csv.reader
- Lê o arquivo como linhas de listas.
- Exemplo: `for linha in leitor:`.

## csv.DictReader
- Lê cada linha como dicionário.
- Usa os cabeçalhos do arquivo como chaves.

## pandas
- `pd.read_csv()` carrega dados em um DataFrame.
- Facilita análise e limpeza.

## Limpeza de dados
- Remova espaços extras com `.strip()`.
- Converta tipos com `int()` ou `float()`.
- Trate valores ausentes e inconsistentes.
