# Capítulo 15 — Simulações e gráficos (detalhado)

1) Simular rolamento de dados

```python
import random
rolls = [random.randint(1,6) for _ in range(1000)]
```

2) Plotar com matplotlib

```python
import matplotlib.pyplot as plt
plt.hist(rolls, bins=6)
plt.show()
```

Dica: use muitas repetições para estimativas estatísticas mais estáveis.
