import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Observe eventos do teclado e do mouse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redesenhe a tela a cada passagem pelo loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Torne a tela desenhada mais recentemente visível.
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Crie uma instância do jogo e execute-o.
    ai = AlienInvasion()
    ai.run_game()