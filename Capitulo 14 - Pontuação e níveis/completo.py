"""Capítulo 14: Pontuação e níveis
Este arquivo mostra forma básica de pontuação e subida de nível.
"""

pontuacao = 0
nivel = 1

aumentar = 15
pontuacao += aumentar
print('Pontuação:', pontuacao)

if pontuacao >= 10:
    nivel += 1
    print('Subiu de nível para', nivel)

botao_play = True
if botao_play:
    print('O jogo começa quando o botão play for usado')
