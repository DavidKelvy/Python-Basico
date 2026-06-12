# Capítulo 10 — Arquivos e exceções (detalhado)

1) Leitura com `with`

```python
with open('arquivo.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
```

2) Escrita

```python
with open('out.txt', 'w', encoding='utf-8') as f:
    f.write('linha\n')
```

3) JSON

```python
import json
with open('dados.json') as f:
    obj = json.load(f)
```

4) Tratamento de exceções

```python
try:
    1/0
except ZeroDivisionError:
    print('Divisão por zero')
```

Dica: sempre especifique exceções esperadas ao tratar erros.
