# Exemplo 1: Atualizar pontos
pontuacao = 0
pontuacao += 10
pontuacao += 20
print(pontuacao)

# Exemplo 2: Verificar nível
nivel = 1
if pontuacao >= 50:
    nivel += 1
print(nivel)

# Exemplo 3: Dificuldade
inimigos = nivel * 3
print('Inimigos:', inimigos)

# Exemplo 4: Próxima meta
meta = nivel * 100
print('Meta:', meta)
