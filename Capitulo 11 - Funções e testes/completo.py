"""Capítulo 11: Funções e testes
Este arquivo mostra funções e exemplos de testes simples.
"""

def saudacao(nome):
    return f'Olá, {nome}!'

assert saudacao('Ana') == 'Olá, Ana!'
print('Teste de saudacao passou')


def soma(a, b):
    return a + b

assert soma(2, 3) == 5
print('Teste de soma passou')
