import pygame
import sys
from modulos.gargola import Gargola
from modulos.comecocos import Comecocos

class JuegoGargola:
    #Clase para gestionar el cohete

    def __init__ (self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Gárgola!")
        self.bg_colour = (230, 230, 230)
        self.gargola = Gargola(self)

    def run_game (self):
        while True:
            self._update_screen()
            self.gargola.update()
            self.clock.tick(600)
            self._check_events()
            

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
        if event.key == pygame.K_RIGHT:
            self.gargola.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.gargola.moving_left = True
        elif event.key == pygame.K_UP:
            self.gargola.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.gargola.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events (self, event):
        #Responde a liberaciones de teclas
        if event.key == pygame.K_RIGHT:
            self.gargola.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.gargola.moving_left = False
        elif event.key == pygame.K_UP:
            self.gargola.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.gargola.moving_down = False

    def _update_screen (self):
            self.screen.fill(self.bg_colour)
            self.gargola.blitme()
            pygame.display.flip()



if __name__ == '__main__':
    g = JuegoGargola()
    g.run_game()