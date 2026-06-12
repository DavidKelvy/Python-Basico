"""Capítulo 01: Tuplas e conjuntos

Este arquivo mostra o uso básico de tuplas e conjuntos em Python.
"""

# Tuplas são imutáveis e úteis para agrupar valores relacionados.
coordenadas = (10, 20)
nome_e_idade = ('Ana', 28)
print('Coordenadas:', coordenadas)
print('Nome:', nome_e_idade[0])
print('Idade:', nome_e_idade[1])

# Tentar alterar uma tupla causa erro.
try:
    coordenadas[0] = 15
except TypeError as erro:
    print('Erro:', erro)

# Conjuntos armazenam valores únicos e não têm ordem fixa.
cores = {'vermelho', 'verde', 'azul', 'verde'}
print('Conjunto de cores:', cores)
print('Quantidade de cores:', len(cores))

# Operações com conjuntos.
mais_cores = {'amarelo', 'azul', 'roxo'}
print('União:', cores | mais_cores)
print('Interseção:', cores & mais_cores)
print('Diferença:', cores - mais_cores)

# Convertendo lista para tupla e conjunto.
valores = [1, 2, 2, 3, 4]
print('Lista original:', valores)
print('Tupla:', tuple(valores))
print('Conjunto:', set(valores))
