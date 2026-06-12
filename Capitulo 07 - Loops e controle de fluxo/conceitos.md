# Capítulo 07 — Loops e controle de fluxo (detalhado)

1) `enumerate` e `zip`

```python
nomes = ['Ana', 'Bruno']
idades = [30, 25]
for i, (n, idd) in enumerate(zip(nomes, idades)):
	print(i, n, idd)
```

2) Loop sentinel e validação de entrada

```python
while True:
	s = input('Digite sair para terminar: ')
	if s == 'sair':
		break
```

3) `for/else` (executa `else` se não houve `break`)

Dica: prefira loops claros e evite mutações desnecessárias durante iterações.
