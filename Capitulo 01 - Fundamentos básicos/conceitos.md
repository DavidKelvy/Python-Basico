# Capítulo 01 — Fundamentos básicos (detalhado)

Descrição: conceitos essenciais e exemplos simples.

1) print()
- Descrição: imprime texto no terminal.
- Exemplo:

```python
print('Olá, mundo!')
```

2) Comentários
- Descrição: explicam o código; começam com `#`.
- Exemplo:

```python
# Isto é um comentário
x = 5  # comentário após código
```

3) Variáveis e tipos básicos
- `int`, `float`, `str`, `bool`.
- Exemplo:

```python
idade = 30          # int
altura = 1.75       # float
nome = 'Ana'        # str
ativo = True        # bool
```

4) Conversão de tipos

```python
n = input('Idade: ')
idade = int(n)
```

5) Operadores aritméticos

```python
soma = 2 + 3
resto = 7 % 3
pot = 2 ** 3
```

6) Entrada do usuário
- `input()` sempre retorna `str`; converta quando necessário.

7) Expressões booleanas e condicionais

```python
if idade >= 18:
	print('Adulto')
else:
	print('Menor')
```

8) Funções simples

```python
def saudacao(nome):
	return f'Olá, {nome}!'

print(saudacao('Ana'))
```

9) Laços básicos

```python
for i in range(5):
	print(i)

n = 0
while n < 3:
	print(n)
	n += 1
```

10) Tuplas e conjuntos
- `tuple`: imutável—use para dados fixos.
- `set`: coleção sem duplicatas.

11) Ambientes virtuais
- `python -m venv venv` para criar; `venv\\Scripts\\activate` no Windows.

Dica: pratique combinando entrada, conversões e condicionais para consolidar.
