import pygame


class Ship:
    """Uma classe para gerenciar o navio."""

    def __init__(self, ai_game):
        """Inicialize a nave e defina sua posição inicial."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carregue a imagem da nave e obtenha seu rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Inicie cada nova nave no centro inferior da tela.
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazene um float para a posição horizontal exata da nave.
        self.x = float(self.rect.x)

        # Flags de movimento; comece com uma nave que não está se movendo.
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Centralize o navio na tela."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Atualize a posição do navio com base nas bandeiras de movimento."""
        # Atualize o valor x da nave, não o rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        # Atualize o objeto rect a partir de self.x.
        self.rect.x = self.x

    def blitme(self):
        """Desenhe o navio em sua localização atual."""
        self.screen.blit(self.image, self.rect)