"""Exemplos de compreensões, geradores e gerenciamento de contexto.
"""

# Compreensões de lista, conjunto e dicionário
numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros]
pares = {x for x in numeros if x % 2 == 0}
paridade = {x: ('par' if x % 2 == 0 else 'ímpar') for x in numeros}

print('Quadrados:', quadrados)
print('Pares:', pares)
print('Paridade:', paridade)

# Gerador preguiçoso
def gerador_quadrados(n):
    for i in range(n):
        yield i * i

print('Primeiros quadrados do gerador:')
for valor in gerador_quadrados(5):
    print(valor)

# Gerenciador de contexto personalizado
from contextlib import contextmanager

@contextmanager
def abrir_arquivo_temporario(caminho, modo='w'):
    arquivo = open(caminho, modo, encoding='utf-8')
    try:
        yield arquivo
    finally:
        arquivo.close()

with abrir_arquivo_temporario('temp_profissional.txt') as arquivo:
    arquivo.write('Exemplo de context manager em Python.')

print('Arquivo temporário criado com sucesso.')
