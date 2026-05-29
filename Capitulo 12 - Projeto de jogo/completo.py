"""Capítulo 12: Jogo básico
Este arquivo mostra a estrutura de um jogo com loop principal.
"""

import time

jogo_rodando = True
pontuacao = 0

while jogo_rodando:
    print('O jogo está rodando...')
    pontuacao += 10
    if pontuacao >= 30:
        jogo_rodando = False
        print('Fim do jogo! Pontuação:', pontuacao)
    time.sleep(0.1)
