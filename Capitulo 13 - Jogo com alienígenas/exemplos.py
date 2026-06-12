# Exemplo 1: Alienígena representado como dicionário
alien = {'x': 0, 'y': 1, 'vida': 2}
print(alien)

# Exemplo 2: Movimento
def mover(alien, dx, dy):
    alien['x'] += dx
    alien['y'] += dy

mover(alien, 1, 2)
print(alien)

# Exemplo 3: Ataque e pontos
pontuacao = 0
alien['vida'] -= 1
if alien['vida'] <= 0:
    pontuacao += 10
print(alien['vida'], pontuacao)

# Exemplo 4: Colisão
def colide(pos1, pos2):
    return pos1 == pos2
print(colide((1, 1), (1, 1)))
