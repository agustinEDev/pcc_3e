import pygame
import sys

from modulos.star import Star

class Four_stars():
    #Clase que inicializa four_stars

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Stars!")
        self.bg_color = (255, 255, 255)
        self.star = Star(self)


    def run_stars (self):
        #Inicializamos la pantalla
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            
            for i in range(4):
                self.screen.fill(self.bg_color)
                self.star.blitme(i)
                pygame.display.flip()
            self.clock.tick(60)


stars = Four_stars()
stars.run_stars()