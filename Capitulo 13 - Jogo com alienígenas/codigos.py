class Alien:
    def __init__(self, x, y, vida):
        self.x = x
        self.y = y
        self.vida = vida

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def sofrer_dano(self, dano):
        self.vida -= dano

    def esta_vivo(self):
        return self.vida > 0

class Jogador:
    def __init__(self):
        self.pontuacao = 0

    def atacar(self, alien):
        alien.sofrer_dano(1)
        if not alien.esta_vivo():
            self.pontuacao += 10

alien = Alien(0, 0, 3)
player = Jogador()
player.atacar(alien)
player.atacar(alien)
player.atacar(alien)
print(alien.vida)
print(alien.esta_vivo())
print(player.pontuacao)
