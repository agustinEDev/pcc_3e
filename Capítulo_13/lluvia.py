import pygame
import sys

from random import randint
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
        self.gotas = pygame.sprite.Group()
        self._create_gotas()

    def run_lluvia (self):
        #Inicializa el bucle principal para el juego.
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self._update_gotas()
            self._update_screen()
            self.clock.tick(30)

    def _update_gotas (self):
        #Actualiza la posición de las gotas en la pantalla.
        for gota in self.gotas.sprites():
            gota.update()
            if gota.rect.top >= self.screen_rect.bottom + gota.rect.height:
                gota.reset()

    def _update_screen (self):
        #Actualiza las imágenes en la pantalla y voltea a la nueva pantalla.
        self.screen.fill(self.bg_color)
        self.gotas.draw(self.screen)
        pygame.display.flip()

    def _create_gotas (self):
        #Llena la pantalla con gotas.
        switch = randint(0, 1)
        gota = Gota(self)
        gota_width, gota_height = gota.rect.size
        
        current_x, current_y = 0, self.screen_rect.y - gota_height
        while current_y <= self.screen_rect.height:
            while current_x <= self.screen_rect.width:
                if switch == 0:
                    self._create_gota(current_x, current_y)
                current_x += gota_width

            #Al acabar la fila, se mueve al inicio de la siguiente.
            current_x = 0
            current_y += gota_height

    def _create_gota (self, x_position, y_position):
        #Crea una gota y la añade al grupo de gotas.
        gota = Gota(self)
        gota.x = x_position
        gota.y = y_position
        gota.rect.x = gota.x
        gota.rect.y = gota.y
        self.gotas.add(gota)

if __name__ == '__main__':
    #Crea una instancia de la clase y ejecuta el juego.
    lluvia = Lluvia()
    lluvia.run_lluvia() 