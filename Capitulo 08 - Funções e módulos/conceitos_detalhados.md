# Capítulo 08 — Funções e módulos (detalhado)

1) Definindo funções

```python
def soma(a, b=0):
    return a + b
```

2) `*args` e `**kwargs`

```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)
```

3) Módulos e imports
- `import modulo`, `from modulo import func`, `import modulo as m`.

4) `__name__ == '__main__'`

```python
if __name__ == '__main__':
    # código de execução direta
    pass
```

Dica: escreva docstrings e mantenha funções pequenas e testáveis.
