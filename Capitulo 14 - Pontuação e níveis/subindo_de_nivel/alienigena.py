try:
    import pygame
except ImportError:
    raise ImportError("Módulo 'pygame' não encontrado. Instale com: pip install pygame") from None

from pygame.sprite import Sprite


class Alien(Sprite):
    """Uma classe para representar um único alienígena na frota."""

    def __init__(self, ai_game):
        """Inicialize o alienígena e defina sua posição inicial."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carregue a imagem do alienígena e defina seu atributo rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicie cada novo alienígena próximo ao canto superior esquerdo da tela.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazene a posição horizontal exata do alienígena.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Retorna True se o alienígena estiver na borda da tela."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Mova o alienígena para a direita ou para a esquerda."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x