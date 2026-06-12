"""Capítulo 01: Condições e lógicos
Este arquivo mostra comparações, booleanos e estruturas if/else.
"""

# Comparações simples
print('5 > 3?', 5 > 3)
print('4 < 2?', 4 < 2)
print('7 == 7?', 7 == 7)
print('8 != 5?', 8 != 5)

# Operadores lógicos
print('Verdadeiro e Falso:', True and False)
print('Verdadeiro ou Falso:', True or False)
print('Não Verdadeiro:', not True)

# condição básica
numero = 12
if numero % 2 == 0:
    print(numero, 'é par')
else:
    print(numero, 'é ímpar')

# condição com elif
nota = 7
if nota >= 7:
    print('Aprovado')
elif nota >= 4:
    print('Recuperação')
else:
    print('Reprovado')

# Combinação de condições
idade = 20
tem_carteira = True
if idade >= 18 and tem_carteira:
    print('Pode dirigir')
else:
    print('Não pode dirigir')

# Teste de presença
frutas = ['maçã', 'banana', 'laranja']
if 'banana' in frutas:
    print('Banana está na lista')
