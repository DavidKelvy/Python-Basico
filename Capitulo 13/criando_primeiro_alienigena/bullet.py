import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Crie um rect de projétil em (0, 0) e depois defina a posição correta.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Armazene a posição do projétil como float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Atualize a posição exata do projétil.
        self.y -= self.settings.bullet_speed
        # Atualize a posição do rect.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)