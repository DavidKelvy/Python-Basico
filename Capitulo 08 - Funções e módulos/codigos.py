def saudacao(nome, saudacao='Olá'):
    return f'{saudacao}, {nome}!'

def soma(a, b=0):
    return a + b

resultado1 = saudacao('Lucas')
resultado2 = saudacao('Mariana', 'Bom dia')
valor1 = soma(3, 7)
valor2 = soma(5)

import math
import random

raiz = math.sqrt(16)
aleatorio = random.randint(1, 10)
print(resultado1)
print(resultado2)
print(valor1)
print(valor2)
print(raiz)
print(aleatorio)
