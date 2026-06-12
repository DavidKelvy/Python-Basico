# Capítulo 12 — Projeto de jogo

Conceitos usados no projeto de jogo (baseado em Pygame):

- **estrutura do projeto**: separar `settings`, `main` e módulos (`nave`, `bullet`).
- **inicialização do Pygame**: `pygame.init()` e criação da janela com `pygame.display.set_mode()`.
- **loop do jogo**: evento principal que processa entradas, atualiza estado e desenha tela repetidamente.
- **event loop**: lidar com `pygame.event.get()` para teclas, fechamento e ações do usuário.
- **sprites e imagens**: carregar imagens (`.bmp`) e desenhar com `blit()`; usar `Rect` para posicionamento e colisões.
- **controle de taxa de quadros**: `pygame.time.Clock()` para limitar FPS.
- **módulo de configurações**: centralizar constantes (tamanhos, cores, velocidade) em `settings.py`.

Esses conceitos formam a base de um jogo simples com Pygame.
