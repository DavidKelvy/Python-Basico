# Capítulo 12 — Projeto de jogo

Este capítulo mostra como construir um jogo básico com Pygame.

## pygame.init()
- Inicializa os módulos do Pygame.

## Tela
- `pygame.display.set_mode((largura, altura))` cria a janela.

## Loop principal
- Repetição principal do jogo.
- Atualiza lógica, trata eventos e desenha a tela.

## Eventos
- `pygame.event.get()` retorna eventos de teclado, mouse e janela.
- Trate `QUIT` para fechar o jogo.

## Sprites
- Objetos do jogo que podem ser desenhados e atualizados.
- Facilita organizar inimigos, jogador e projéteis.
