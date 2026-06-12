# Exemplo 1: Criar função
def dobro(valor):
    return valor * 2
print(dobro(5))

# Exemplo 2: Parâmetros padrão
def saudacao(nome='visitante'):
    return f'Olá, {nome}!'
print(saudacao())
print(saudacao('Luna'))

# Exemplo 3: Testes
assert dobro(2) == 4
assert saudacao('Ana') == 'Olá, Ana!'
print('Assert passou')

# Exemplo 4: Filtrar lista
def pares(lista):
    return [x for x in lista if x % 2 == 0]
print(pares([1, 2, 3, 4]))
