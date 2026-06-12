# Exemplo 1: Estado do jogo
game = {'vidas': 3, 'pontos': 0, 'nivel': 1}
print(game)

# Exemplo 2: Atualizar pontuação
game['pontos'] += 25
print(game['pontos'])

# Exemplo 3: Subir de nível
if game['pontos'] >= 50:
    game['nivel'] += 1
print(game['nivel'])

# Exemplo 4: Verificar fim de jogo
if game['vidas'] == 0:
    print('Game Over')
else:
    print('Continue jogando')
