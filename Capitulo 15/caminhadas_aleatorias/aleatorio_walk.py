from random import choice


class RandomWalk:
    """Uma classe para gerar passeios aleatórios."""

    def __init__(self, num_points=5000):
        """Inicialize atributos de uma caminhada."""
        self.num_points = num_points

        # Todas as caminhadas começam em (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcule todos os pontos da caminhada."""
        # Continue dando passos até a caminhada atingir o comprimento desejado.
        while len(self.x_values) < self.num_points:

            # Decida qual direção seguir e até onde ir.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rejeite movimentos que não levam a lugar nenhum.
            if x_step == 0 and y_step == 0:
                continue

            # Calcule a nova posição.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)