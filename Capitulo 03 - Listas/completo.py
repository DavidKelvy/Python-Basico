"""Capítulo 03: Listas
Este arquivo mostra operações comuns com listas em Python.
"""

veiculos = ['bicicleta', 'carro', 'moto']
print('Lista original:', veiculos)
print('Primeiro item:', veiculos[0])
print('Último item:', veiculos[-1])

veiculos.append('ônibus')
print('Depois de append:', veiculos)

veiculos.insert(1, 'patinete')
print('Depois de insert:', veiculos)

veiculos.remove('carro')
print('Depois de remove:', veiculos)

item = veiculos.pop()
print('Removido com pop:', item)
print('Agora:', veiculos)

veiculos.sort()
print('Ordenados:', veiculos)

frutas = ['maçã', 'banana', 'laranja', 'uva']
print('Fatia:', frutas[1:3])
