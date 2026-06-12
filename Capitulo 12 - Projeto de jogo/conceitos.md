# Capítulo 12 — Projeto de jogo (detalhado)

1) Estrutura e `settings`
- Centralize constantes (tamanho da tela, cores, velocidades).

2) Loop principal

```python
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# atualizar estado
	# desenhar tela
	pygame.display.flip()
```

3) Sprites e colisões
- Use `pygame.sprite.Sprite` e `Group` para organizar atualizações e desenho.

Dica: mantenha atualização de lógica e desenho separados para clareza.
