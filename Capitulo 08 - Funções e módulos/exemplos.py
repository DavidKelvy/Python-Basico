# Exemplo 1: Função simples
def dobrar(valor):
    return valor * 2
print(dobrar(4))

# Exemplo 2: Parâmetro padrão
def apresentar(nome='visitante'):
    return f'Olá, {nome}!'
print(apresentar())
print(apresentar('Rita'))

# Exemplo 3: Importar módulo
import math
print(math.pi)
print(math.factorial(5))

# Exemplo 4: Função por nome
def soma(a, b):
    return a + b
print(soma(b=2, a=3))

# Exemplo 5: Retornar lista
def pares_ate(n):
    return [x for x in range(1, n + 1) if x % 2 == 0]
print(pares_ate(10))
