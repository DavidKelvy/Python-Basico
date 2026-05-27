import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Continue fazendo novas caminhadas enquanto o programa estiver ativo.
while True:
    # Faça uma caminhada aleatória.
    rw = RandomWalk()
    rw.fill_walk()

    # Trace os pontos da caminhada.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=15)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("Fazer outra caminhada? (s/n): ")
    if keep_running == 'n':
        break