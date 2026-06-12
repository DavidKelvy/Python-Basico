class Settings:
    """Uma classe para armazenar todas as configurações de Alien Invasion."""

    def __init__(self):
        """Inicialize as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configurações da nave.
        self.ship_speed = 1.5