"""Capítulo 15: Rolando dados
Este complemento mostra como simular lançamentos de dados e contar resultados.
"""

from random import randint

dados = [randint(1, 6) for _ in range(10)]
print('Lançamentos:', dados)

frequencia = {}
for valor in dados:
    frequencia[valor] = frequencia.get(valor, 0) + 1
print('Frequências:', frequencia)
