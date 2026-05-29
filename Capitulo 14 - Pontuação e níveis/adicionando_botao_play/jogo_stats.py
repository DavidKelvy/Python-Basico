class GameStats:
    """Acompanhe as estatísticas da invasão alienígena."""

    def __init__(self, ai_game):
        """Inicialize estatísticas."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Inicialize estatísticas que podem mudar durante o jogo."""
        self.ships_left = self.settings.ship_limit