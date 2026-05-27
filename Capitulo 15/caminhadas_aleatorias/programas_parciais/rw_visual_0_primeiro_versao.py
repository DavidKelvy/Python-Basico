import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Faça uma caminhada aleatória.
rw = RandomWalk()
rw.fill_walk()

# Trace os pontos da caminhada.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
plt.show()