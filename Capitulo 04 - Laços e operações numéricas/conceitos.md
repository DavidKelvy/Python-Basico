# Capítulo 04 — Laços e operações numéricas (detalhado)

1) `for` com `range`

```python
for i in range(1, 6):
	print(i)
```

2) `while`

```python
n = 0
while n < 3:
	print(n)
	n += 1
```

3) `break` e `continue`

```python
for i in range(10):
	if i == 5:
		break
	if i % 2 == 0:
		continue
	print(i)
```

4) Operações numéricas e `math`

```python
import math
print(math.sqrt(16))
```

Dica: use `enumerate` e `zip` para iterar com índices e múltiplas sequências.
