"""Capítulo 07: Laços e controle de fluxo
Este arquivo mostra while, for, continue e break.
"""

for i in range(1, 6):
    if i == 4:
        print('Pulando o 4')
        continue
    print('Loop for:', i)

contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        print('Parando no 3')
        break
    print('Loop while:', contador)

animais = ['gato', 'cachorro', 'papagaio']
for animal in animais:
    print('Animal:', animal)
