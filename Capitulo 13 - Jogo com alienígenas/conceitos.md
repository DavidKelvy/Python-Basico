# Capítulo 13 — Jogo com alienígenas (detalhado)

1) Movimento de frota
- Calcular limites e inverter direção ao atingir borda.

2) Colisões e remoção segura

```python
hits = pygame.sprite.groupcollide(balas, aliens, True, True)
```

3) Estados de jogo (vidas, reiniciar)

Dica: trate criação e destruição de sprites fora do loop principal quando possível.
