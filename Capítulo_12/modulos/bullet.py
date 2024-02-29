import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #Una clase pra gestionar las balas disparadas desde la nave.

    def __init__ (self, ai_game):
        #Crea un objeto bala en la posición actual de la nave.
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Crea un rectángulo para la bala en (0,0) y luego establece la posición correcta.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midleft = ai_game.gargola.rect.midleft

        #Guarda la posición de la bala como float
        self.x = float(self.rect.x)

    def update (self):
        #Mueve la bala hacia arriba por la pantalla
        #Actualiza la posición exacta de la bala
        self.x -= self.settings.bullet_speed
        #Actualiza la posición del rectángulo
        self.rect.x = self.x
    
    def draw_bullet (self):
        #Dibuja la bala en pantalla
        pygame.draw.rect(self.screen, self.color, self.rect)

    def remove_bullet (self):
        #Elimina la bala de la pantalla
        self.bullets.remove(bullet)
        self.bullets.remove(bullet)
        #print(len(self.bullets))