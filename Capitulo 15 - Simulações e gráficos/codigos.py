import math

trajetoria = []
for t in range(0, 11):
    x = t
    y = 10 + 5 * t - 0.5 * 9.8 * t ** 2
    trajetoria.append((x, y))
valores = [math.sin(x / 10) for x in range(0, 31)]
print('Trajetória:', trajetoria)
print('Senoides:', valores)
