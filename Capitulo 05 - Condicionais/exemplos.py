# Exemplo 1: Ímpar ou par
numero = 7
if numero % 2 == 0:
    print('par')
else:
    print('ímpar')

# Exemplo 2: Faixas de nota
pontuacao = 72
if pontuacao >= 90:
    print('excelente')
elif pontuacao >= 70:
    print('bom')
else:
    print('precisa melhorar')

# Exemplo 3: Operadores lógicos
a = True
b = False
if a and not b:
    print('Condição satisfeita')

# Exemplo 4: Expressão condicional
texto = 'aprovado' if pontuacao >= 70 else 'reprovado'
print(texto)

# Exemplo 5: Comparação composta
x = 15
if 10 < x <= 20:
    print('x está entre 11 e 20')
