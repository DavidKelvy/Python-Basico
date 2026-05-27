import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Continue fazendo novas caminhadas enquanto o programa estiver ativo.
while True:
    # Faça uma caminhada aleatória.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Trace os pontos da caminhada.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
       edgecolors='none', s=1)
    ax.set_aspect('equal')

    # Enfatize o primeiro e o último ponto.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)

    # Remova os eixos.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Fazer outra caminhada? (s/n): ")
    if keep_running == 'n':
        break