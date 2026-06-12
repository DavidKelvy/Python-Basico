# Exemplo 1: Queda livre
for tempo in range(0, 6):
    altura = 100 - 4.9 * tempo ** 2
    print('tempo', tempo, 'altura', altura)

# Exemplo 2: Movimento linear
for passo in range(5):
    posicao = passo * 2
    print(posicao)

# Exemplo 3: Valores trigonométricos
import math
valores = [math.sin(math.radians(angulo)) for angulo in range(0, 181, 30)]
print(valores)

# Exemplo 4: Dados para gráfico
dados = [(x, x ** 2) for x in range(6)]
print(dados)
