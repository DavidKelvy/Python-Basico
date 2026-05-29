"""Capítulo 03: Listas e métodos de lista
Este complemento reúne formas comuns de trabalhar com listas em Python.
"""

# Criar listas e acessar elementos
bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas[0])
print(bicicletas[-1])

# Adicionar itens
bicicletas.append('giant')
if 'cannondale' in bicicletas:
    bicicletas.insert(1, 'kona')

# Remover itens
bicicletas.remove('redline')
ultima = bicicletas.pop()
print('Removido:', ultima)

# Ordenar e inverter
bicicletas.sort()
print('Ordenadas:', bicicletas)
bicicletas.reverse()
print('Invertidas:', bicicletas)

# Percorrer listas
for bicicleta in bicicletas:
    print('Eu queria uma', bicicleta)

for indice, bicicleta in enumerate(bicicletas, start=1):
    print(f'{indice}. {bicicleta}')

# Compreensão de lista
numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros]
print('Quadrados:', quadrados)
