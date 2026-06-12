"""Capítulo 01: Entrada de usuário
Este arquivo mostra como ler dados do teclado e usar valores em cálculos.
"""

nome = input('Qual é o seu nome? ')
print(f'Olá, {nome}!')

idade = int(input('Quantos anos você tem? '))
print(f'Você nasceu em {2024 - idade}.')

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
print(f'Soma: {numero1 + numero2}')
print(f'Subtração: {numero1 - numero2}')
print(f'Multiplicação: {numero1 * numero2}')
print(f'Divisão: {numero1 / numero2}')
