def soma(a, b):
    return a + b

def maior(a, b):
    return a if a >= b else b

def eh_par(n):
    return n % 2 == 0

assert soma(2, 3) == 5
assert maior(7, 4) == 7
assert maior(3, 5) == 5
assert eh_par(4) is True
assert eh_par(5) is False
print('Testes básicos executados com sucesso')
