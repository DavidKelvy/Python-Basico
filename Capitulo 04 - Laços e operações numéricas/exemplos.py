# Exemplo 1: Soma com loop
valores = [10, 20, 30]
acumulado = 0
for valor in valores:
    acumulado += valor
print(acumulado)

# Exemplo 2: Pares com range
for n in range(1, 11):
    if n % 2 == 0:
        print(n, 'é par')

# Exemplo 3: Loop while
contador = 1
while contador <= 4:
    print(contador)
    contador += 1

# Exemplo 4: Break e continue
for n in range(1, 6):
    if n == 2:
        continue
    if n == 5:
        break
    print(n)

# Exemplo 5: Compreensão numérica
cubos = [x ** 3 for x in range(1, 6)]
print(cubos)
