# Capítulo 16 — Dados e CSV (detalhado)

1) Leitura básica com `csv`

```python
import csv
with open('sitka_weather_2021_simples.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

2) Usando `pandas` para facilitar

```python
import pandas as pd
df = pd.read_csv('sitka_weather_2021_simples.csv')
print(df.head())
```

Dica: verifique o encoding e delimitador do CSV antes de processar.
