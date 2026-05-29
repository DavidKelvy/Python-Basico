"""Capítulo 01: Funções e laços
Este arquivo mostra como definir funções e usar loops básicos.
"""

# Definir função simples

def dobrar(numero):
    return numero * 2

resultado = dobrar(4)
print('Dobro de 4:', resultado)

# Função com dois parâmetros

def somar(a, b):
    return a + b

print('5 + 3 =', somar(5, 3))

# Laço for com range
for i in range(1, 6):
    print('Contador for:', i)

# Laço while
contador = 1
while contador <= 3:
    print('Contador while:', contador)
    contador += 1

# Lista básica
cores = ['vermelho', 'verde', 'azul']
for cor in cores:
    print('Cor:', cor)

# Loop com enumerate para índice
for indice, cor in enumerate(cores, start=1):
    print(f'{indice}. {cor}')
