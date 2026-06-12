# Exemplo 1: Pathlib
from pathlib import Path
arquivo = Path('arquivo.txt')
print(arquivo.exists())
print(arquivo.stem)

# Exemplo 2: Generator expression
quadrados = (n * n for n in range(5))
for valor in quadrados:
    print(valor)

# Exemplo 3: Decorador simples
def mostrar_nome(func):
    def wrapper(*args, **kwargs):
        print('Executando função')
        return func(*args, **kwargs)
    return wrapper

@mostrar_nome
def diga_oi():
    print('Oi')

diga_oi()
