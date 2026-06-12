# Capítulo 21 — Python profissional (detalhado)

1) Pathlib e filesystem

```python
from pathlib import Path
p = Path('arquivo.txt')
print(p.exists())
```

2) SQLite básico

```python
import sqlite3
conn = sqlite3.connect('db.sqlite3')
```

3) Decoradores

```python
def log(func):
    def wrapper(*args, **kwargs):
        print('chamando', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

4) Testes e empacotamento
- `pytest` e `requirements_example.txt`.

Dica: escreva README e exemplos de uso para pacotes que for distribuir.
