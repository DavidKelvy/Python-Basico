# Capítulo 14 — Pontuação e níveis

Este capítulo adiciona objetivos, níveis e interface ao jogo.

## Pontuação
- Um valor que aumenta quando o jogador acerta um inimigo.
- Mostrado na tela durante o jogo.

## Níveis
- Aumentam a dificuldade progressivamente.
- Podem acelerar inimigos ou incluir mais obstáculos.

## Botões
- Detectam cliques do mouse para iniciar ou reiniciar o jogo.
- `pygame.mouse.get_pressed()` retorna o estado dos botões.

## Estado do jogo
- Controle o fluxo com variáveis como `jogo_ativo`.
- Evite executar lógica de jogo quando o jogo estiver pausado.
