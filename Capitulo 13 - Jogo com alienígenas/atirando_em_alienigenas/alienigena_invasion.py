import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Inicie o loop principal do jogo."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()            

    def _check_keyup_events(self, event):
        """Responda aos principais lançamentos."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Crie um novo marcador e adicione-o ao grupo de marcadores."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Atualize a posição dos marcadores e livre-se dos marcadores antigos."""
        # Atualize as posições dos projéteis.
        self.bullets.update()

        # Livre-se dos projéteis que desapareceram.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        

    def _check_bullet_alien_collisions(self):
        """Responda a colisões entre balas e alienígenas."""
        # Remova quaisquer projéteis e alienígenas que colidiram.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destrua os projéteis existentes e crie nova frota.
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Atualize as posições de todos os alienígenas da frota."""
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """Crie a frota de alienígenas."""
        # Crie um alienígena e continue adicionando alienígenas até não haver mais espaço.
        # O espaçamento entre os alienígenas é de uma largura alienígena e uma altura alienígena.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Terminou uma linha; redefinir o valor x e incrementar o valor y.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Crie um alienígena e coloque-o na frota."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Responda apropriadamente se algum alienígena chegar ao limite."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Largue toda a frota e mude a direção da frota."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Atualize as imagens na tela e vá para a nova tela."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Crie uma instância do jogo e execute-o.
    ai = AlienInvasion()
    ai.run_game()