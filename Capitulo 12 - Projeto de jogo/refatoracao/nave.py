import pygame


class Ship:
    """Uma classe para gerenciar o navio."""

    def __init__(self, ai_game):
        """Inicialize a nave e defina sua posição inicial."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carregue a imagem da nave e obtenha seu rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Inicie cada nova nave no centro inferior da tela.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Desenhe o navio em sua localização atual."""
        self.screen.blit(self.image, self.rect)