"""Capítulo 15: Caminhadas aleatórias
Este complemento mostra como gerar uma caminhada aleatória e registrar os passos.
"""

from random import choice

posicao = 0
passos = [posicao]
for _ in range(10):
    movimento = choice([1, -1])
    posicao += movimento
    passos.append(posicao)

print('Posições:', passos)
print('Deslocamento final:', passos[-1])
