"""Capítulo 15: Gráfico de linha simples
Este complemento mostra como preparar dados para plotar uma linha.
"""

x = list(range(1, 11))
y = [valor**2 for valor in x]

for indice, valor in enumerate(y, start=1):
    print(indice, valor)

# Código de plotagem com matplotlib (comentado se matplotlib não estiver instalado)
# import matplotlib.pyplot as plt
# plt.plot(x, y)
# plt.title('Quadrados de 1 a 10')
# plt.xlabel('x')
# plt.ylabel('x**2')
# plt.show()
