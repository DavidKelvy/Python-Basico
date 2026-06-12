# Capítulo 06 — Dicionários e coleções (detalhado)

1) Dicionários

```python
pessoa = {'nome': 'Ana', 'idade': 30}
print(pessoa['nome'])
print(pessoa.get('altura', 'não informado'))
```

2) Métodos úteis
- `.keys()`, `.values()`, `.items()`, `.update()`.

3) Estruturas aninhadas

```python
usuarios = [{'nome': 'Ana'}, {'nome': 'Bruno'}]
```

4) Sets e tuplas
- `set` para coleções sem duplicatas; `tuple` para imutabilidade.

Dica: use `dict.get()` para evitar exceções quando a chave pode faltar.
