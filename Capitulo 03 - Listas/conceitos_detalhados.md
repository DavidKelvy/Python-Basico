# Capítulo 03 — Listas (detalhado)

1) Criando listas

```python
frutas = ['maçã', 'banana', 'laranja']
```

2) Acessando e modificando

```python
print(frutas[0])
frutas.append('uva')
frutas[1] = 'manga'
```

3) Remover elementos
- `.remove(value)`, `.pop(index)`.

4) Ordenação e cópia

```python
nums = [3,1,2]
nums.sort()
nums_copy = nums[:]  # cópia independente
```

5) Iteração e `enumerate`

```python
for i, v in enumerate(frutas):
    print(i, v)
```

6) Compreensões de lista

```python
quadrados = [x**2 for x in range(6)]
```

Dica: prefira compreensões quando a lógica for simples e legível.
