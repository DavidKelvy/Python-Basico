"""Capítulo 04: Laços e operações numéricas
Este complemento mostra diferentes formas de usar loops e trabalhar com números.
"""

# For com range
for numero in range(1, 6):
    print('Número:', numero)

# Somar valores com loop
soma = 0
for numero in range(1, 11):
    soma += numero
print('Soma de 1 a 10:', soma)

# Construir lista de valores
numeros = [x for x in range(1, 11)]
print('Números:', numeros)

# Usar while
contador = 1
while contador <= 5:
    print('Contador:', contador)
    contador += 1

# Listas e fatiamento
nomes = ['ana', 'bia', 'carlos', 'daniel']
print('Primeiros dois:', nomes[:2])
print('Últimos dois:', nomes[-2:])

# Trabalhar com múltiplas listas
cores = ['vermelho', 'verde', 'azul']
for nome, cor in zip(nomes, cores):
    print(f'{nome} gosta de {cor}')
