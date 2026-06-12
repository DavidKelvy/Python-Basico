# Capítulo 05 — Condicionais (detalhado)

1) `if/elif/else`

```python
x = 10
if x < 0:
    print('negativo')
elif x == 0:
    print('zero')
else:
    print('positivo')
```

2) Operadores lógicos

```python
a = True
b = False
print(a and b)
print(a or b)
print(not a)
```

3) `in` e testes de pertinência

```python
if 'a' in 'casa':
    print('tem a')
```

4) Valores truthy/falsy

- Strings vazias, listas vazias, `0`, `None` são avaliados como `False`.

Dica: escreva condições claras e use funções auxiliares para lógica complexa.
