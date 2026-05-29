"""Exemplos de decoradores e ideias de metaprogramação.
"""

from functools import wraps
import time


def calcular_tempo(func):
    inicio = time.perf_counter()
    resultado = func()
    fim = time.perf_counter()
    return fim - inicio


def decorador_mensagem(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Executando {func.__name__}...')
        resultado = func(*args, **kwargs)
        print(f'Finalizado {func.__name__}!')
        return resultado
    return wrapper


def medidor_tempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        print(f'{func.__name__} levou {fim - inicio:.6f} segundos')
        return resultado
    return wrapper


@decorador_mensagem
@medidor_tempo
def calcular_cubo(valor):
    return valor ** 3


@medidor_tempo
def soma(a, b):
    return a + b


print('Cubo de 4:', calcular_cubo(4))
print('Soma de 7 + 3:', soma(7, 3))

# Decorador de fábrica de validação simples

def validar_positivos(nome_arg):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] < 0:
                raise ValueError(f'{nome_arg} deve ser positivo')
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validar_positivos('valor')
def raiz_quadrada(valor):
    return valor ** 0.5

print('Raiz de 16:', raiz_quadrada(16))
