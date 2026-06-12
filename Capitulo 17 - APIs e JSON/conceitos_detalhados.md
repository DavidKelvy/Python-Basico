# Capítulo 17 — APIs e JSON (detalhado)

1) Requisições HTTP com `requests`

```python
import requests
r = requests.get('https://api.github.com')
if r.status_code == 200:
    data = r.json()
```

2) Manipular JSON
- A resposta `json()` vira `dict`/`list` em Python.

Dica: trate erros de rede e adicione `timeout` nas requisições.
