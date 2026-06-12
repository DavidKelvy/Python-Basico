# Exemplo 1: Dicionário simples
pessoa = {'nome': 'Pedro', 'idade': 34}
print(pessoa['nome'])

# Exemplo 2: Atualizar e remover
pessoa['idade'] = 35
pessoa.pop('idade')
print(pessoa)

# Exemplo 3: Tupla
coordenadas = (10.5, 20.3)
print(coordenadas)

# Exemplo 4: Conjunto
frutas = {'maçã', 'banana', 'maçã'}
print(frutas)

# Exemplo 5: Interseção
a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
print(a.intersection(b))
