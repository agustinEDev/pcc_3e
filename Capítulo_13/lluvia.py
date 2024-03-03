import pygame
import sys

from pygame.sprite import Sprite
from modulos.gota import Gota

class Lluvia:
    #Una clase que representa una gota de lluvia.

    def __init__ (self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        self.bg_color = (255, 255, 255)
        self.gota = Gota(self)

    def run_lluvia (self):
        #Inicializa el bucle principal para el juego.
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self._update_gota()
            self._update_screen()
            self.clock.tick(60)

    def _update_gota (self):
        #Actualiza la posición de las gotas en la pantalla.
            self.gota.update()
            if self.gota.rect.top >= self.screen_rect.bottom + self.gota.rect.height:
                self.gota.reset()

    def _update_screen (self):
        #Actualiza las imágenes en la pantalla y voltea a la nueva pantalla.
        self.screen.fill(self.bg_color)
        self.gota.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    #Crea una instancia de la clase y ejecuta el juego.
    lluvia = Lluvia()
    lluvia.run_lluvia() 