import pygame
import sys
from pygame.sprite import Sprite
from modulos.gargola import Gargola
from modulos.bullet import Bullet
from modulos.settings import Settings

class Tirador():

    def __init__ (self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Tirador lateral")
        self.clock = pygame.time.Clock()
        self.bg_color = (230, 230, 230)
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()
        self.gargola = Gargola(self)
        self.bullets = pygame.sprite.Group()

    def run_tirador(self):
        while True:
            self._update_screen()
            self.gargola.update()
            self.clock.tick(60)
            self._check_events()
            self._update_bullets()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events (self, event):
        #Responde a pulsaciones de teclas
        if event.key == pygame.K_UP:
            self.gargola.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.gargola.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events (self, event):
        #Responde a liberaciones de teclas
        if event.key == pygame.K_UP:
            self.gargola.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.gargola.moving_down = False

    def _fire_bullet (self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets (self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left <= self.screen_rect.left:
                self.bullets.remove(bullet)

    def _update_screen (self):
        self.screen.fill(self.bg_color)
        self.gargola.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
        self.clock.tick(60)

""" ------------------- Main ------------------- """

t = Tirador()
t.run_tirador()
