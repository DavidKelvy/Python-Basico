"""Capítulo 15: Simulações e gráficos
Este arquivo mostra simulações simples de dados e caminhadas.
"""

from random import randint, choice

rolamentos = [randint(1, 6) for _ in range(10)]
print('Dados:', rolamentos)

freq = {}
for valor in rolamentos:
    freq[valor] = freq.get(valor, 0) + 1
print('Frequência:', freq)

posicao = 0
passos = [posicao]
for _ in range(10):
    passo = choice([1, -1])
    posicao += passo
    passos.append(posicao)
print('Caminhada:', passos)
