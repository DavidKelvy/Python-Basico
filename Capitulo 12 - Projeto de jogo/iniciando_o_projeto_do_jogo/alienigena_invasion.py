import sys

try:
    import pygame
except ImportError:
    raise ImportError("Módulo 'pygame' não encontrado. Instale com: pip install pygame") from None

from settings import Settings


class AlienInvasion:
    """Aula geral para gerenciar recursos e comportamento do jogo."""

    def __init__(self):
        """Inicialize o jogo e crie recursos de jogo."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Inicie o loop principal do jogo."""
        while True:
            # Observe eventos do teclado e do mouse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redesenhe a tela a cada passagem pelo loop.
            self.screen.fill(self.settings.bg_color)

            # Torne a tela desenhada mais recentemente visível.
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Crie uma instância do jogo e execute-o.
    ai = AlienInvasion()
    ai.run_game()