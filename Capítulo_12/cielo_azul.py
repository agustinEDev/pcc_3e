import sys
import pygame

class VentanaAzul:

    def __init__ (self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.pantalla = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Ventana Azul")
        self.bg_color = (50, 0, 200)
        
    def run_ventana (self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.pantalla.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

va = VentanaAzul()
va.run_ventana()