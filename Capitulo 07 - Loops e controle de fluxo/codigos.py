nomes = ['Ana', 'Bruno', 'Carla']
for indice, nome in enumerate(nomes, 1):
    print(indice, nome)

pares = []
for n in range(1, 11):
    if n % 2 != 0:
        continue
    pares.append(n)
else:
    print('Loop for finalizado')

contador = 0
while contador < 5:
    if contador == 3:
        break
    contador += 1
print(pares)
