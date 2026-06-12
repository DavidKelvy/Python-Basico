# Capítulo 11 — Funções e testes (detalhado)

1) Escrevendo testes com `pytest`

```python
# teste_funcao.py
from modulo import soma

def test_soma():
    assert soma(2,3) == 5
```

2) `assert` e mensagens claras

Dica: cada teste deve validar uma única hipótese e ser independente.
