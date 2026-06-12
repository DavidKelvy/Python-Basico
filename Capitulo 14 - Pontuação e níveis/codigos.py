def calcular_pontuacao(resultado, bonus=0):
    base = resultado * 10
    return base + bonus

def atualizar_nivel(pontuacao, nivel):
    meta = nivel * 50
    if pontuacao >= meta:
        nivel += 1
    return nivel

def exibir_status(pontuacao, nivel, recorde):
    print(f'Pontuação atual: {pontuacao}')
    print(f'Nível atual: {nivel}')
    print(f'Recorde: {recorde}')

pontuacao = 0
nivel = 1
recorde = 120
for rodada in range(1, 7):
    pontos_ganhos = calcular_pontuacao(rodada, bonus=5)
    pontuacao += pontos_ganhos
    nivel = atualizar_nivel(pontuacao, nivel)
    print(f'Rodada {rodada}: ganhou {pontos_ganhos} pontos')

recorde = max(pontuacao, recorde)
exibir_status(pontuacao, nivel, recorde)
