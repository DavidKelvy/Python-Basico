import sys

try:
    import pygame
except ImportError:
    raise ImportError("Módulo 'pygame' não encontrado. Instale com: pip install pygame") from None

from settings import Settings
from ship import Ship


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

        self.ship = Ship(self)

    def run_game(self):
        """Inicie o loop principal do jogo."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responda a pressionamentos de teclas e eventos do mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responda aos pressionamentos de tecla."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Responda aos principais lançamentos."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Atualize as imagens na tela e vá para a nova tela."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()


if __name__ == '__main__':
    # Crie uma instância do jogo e execute-o.
    ai = AlienInvasion()
    ai.run_game()