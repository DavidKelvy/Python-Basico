"""Capítulo 08: Pacotes e módulos em Python

Este arquivo mostra como organizar código em módulos e pacotes simples.
"""

# Um módulo simples com funções.

def dizer_ola(nome):
    return f'Olá, {nome}!'


def somar(a, b):
    return a + b


if __name__ == '__main__':
    print(dizer_ola('Lucas'))
    print('2 + 3 =', somar(2, 3))

# Um pacote Python é uma pasta com um arquivo __init__.py.
# Exemplo de estrutura:
# meu_pacote/
#   __init__.py
#   operacoes.py
#   utilidades.py
#
# Dentro de operacoes.py:
# def multiplicar(a, b):
#     return a * b
#
# Dentro de __init__.py:
# from .operacoes import multiplicar
#
# Uso:
# from meu_pacote import multiplicar
# print(multiplicar(3, 4))
