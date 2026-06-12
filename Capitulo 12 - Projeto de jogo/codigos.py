def iniciar_jogo():
    vidas = 3
    pontos = 0
    nivel = 1
    return vidas, pontos, nivel

def atualizar_jogo(pontos, nivel, inimigos):
    pontos += inimigos * 10
    if pontos >= nivel * 50:
        nivel += 1
    return pontos, nivel

def jogo_ativo(vidas):
    return vidas > 0

vidas, pontos, nivel = iniciar_jogo()
vidas -= 1
pontos, nivel = atualizar_jogo(pontos, nivel, 4)
print('Vidas:', vidas)
print('Pontos:', pontos)
print('Nível:', nivel)
print('Jogo ativo:', jogo_ativo(vidas))
