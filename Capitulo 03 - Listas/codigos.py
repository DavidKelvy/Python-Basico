cores = ['vermelho', 'verde', 'azul']
cores.append('amarelo')
cores.insert(1, 'laranja')
cores.remove('verde')
ultimo = cores.pop()
contador = len(cores)
ordenado = sorted(cores)
cores.sort()
cores.reverse()
quadrados = [n * n for n in range(1, 6)]
pares = [n for n in range(1, 11) if n % 2 == 0]
print(cores)
print(ultimo)
print(contador)
print(ordenado)
print(quadrados)
print(pares)
