import pygame
import sys

class Teclas:

    def __init__ (self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Teclas")
        self.bg_color = (0, 100, 0)
        self.fuente = pygame.font.Font(None, 100)

    def run_teclas (self):
        text = ''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    else:
                        text = (f"La tecla pulsada es: {event.unicode}")
                        print(text)

            mensaje = self.fuente.render(text, 1, (255, 255, 255))
            self.screen.fill(self.bg_color)
            self.screen.blit(mensaje, (15, 10))
            pygame.display.flip()
            self.clock.tick(60)

t = Teclas()
t.run_teclas()