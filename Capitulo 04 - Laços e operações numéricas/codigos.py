numeros = [1, 2, 3, 4, 5]
total = 0
for n in numeros:
    total += n
media = total / len(numeros)
pares = [n for n in range(1, 11) if n % 2 == 0]
produto = 1
for n in range(1, 6):
    produto *= n
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue
    if contador == 5:
        break
print('Total:', total)
print('Média:', media)
print('Pares:', pares)
print('Fatorial:', produto)
