# Exemplo 1: Acessar itens
frutas = ['maçã', 'banana', 'uva']
print(frutas[0])
print(frutas[-1])

# Exemplo 2: Adicionar e remover
frutas.append('laranja')
frutas.remove('banana')
print(frutas)

# Exemplo 3: Iterar com for
for fruta in frutas:
    print('Fruta:', fruta)

# Exemplo 4: Compreensão
numeros = [1, 2, 3, 4, 5]
quadrados = [n ** 2 for n in numeros]
print(quadrados)

# Exemplo 5: Ordenação
valores = [9, 3, 6, 1]
valores.sort()
print(valores)
