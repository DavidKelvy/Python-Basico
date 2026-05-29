"""Capítulo 13: Elementos de jogo
Este arquivo mostra como representar inimigos e mover uma frota.
"""

class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, distancia):
        self.x += distancia

fleet = [Alien(x * 10, 0) for x in range(5)]
for alien in fleet:
    alien.mover(5)
    print('Alien em', alien.x, alien.y)
