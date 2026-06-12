"""Capítulo 04: Laços e fluxo de controle
Este arquivo mostra como usar loops e gerar sequências de valores.
"""

for numero in range(1, 6):
    print('Número:', numero)

soma = 0
for numero in range(1, 11):
    soma += numero
print('Soma de 1 a 10:', soma)

pares = [x for x in range(1, 11) if x % 2 == 0]
print('Números pares:', pares)

contador = 1
while contador <= 5:
    print('While contador:', contador)
    contador += 1

nomes = ['Ana', 'Bia', 'Caio']
for indice, nome in enumerate(nomes, start=1):
    print(f'{indice}. {nome}')
