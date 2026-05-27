import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Defina o título do gráfico e rotule os eixos.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Defina o tamanho dos rótulos dos ticks.
ax.tick_params(labelsize=14)

plt.show()