import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Carregue a imagem do alienígena e defina seu atributo rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicie cada novo alienígena próximo ao canto superior esquerdo da tela.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazene a posição horizontal exata do alienígena.
        self.x = float(self.rect.x)