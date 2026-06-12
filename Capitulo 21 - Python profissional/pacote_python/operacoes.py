"""Operações matemáticas básicas do pacote de exemplo."""

def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError('Divisor não pode ser zero')
    return a / b
