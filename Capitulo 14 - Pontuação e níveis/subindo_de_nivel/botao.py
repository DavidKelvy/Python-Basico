try:
    import pygame.font
except ImportError:
    raise ImportError("Módulo 'pygame' não encontrado. Instale com: pip install pygame") from None


class Button:
    """Uma classe para construir botões para o jogo."""

    def __init__(self, ai_game, msg):
        """Inicialize os atributos do botão."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Defina as dimensões e propriedades do botão.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Construa o objeto reto do botão e centralize-o.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # A mensagem do botão precisa ser preparada apenas uma vez.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Transforme a mensagem em uma imagem renderizada e centralize o texto no botão."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Desenhe o botão em branco e depois desenhe a mensagem."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)