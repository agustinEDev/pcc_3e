import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #Una clase que representa un solo alien en la flota.

    def __init__(self, ai_game):
        #Inicializa el alien y establece su posición inicial.
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Carga la imagen del alien y establece su atributo rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Inicia un nuevo alien cerca de la posición superior izquierda de la pantalla.
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        #Guarda la posición horizontal exacta del alien.
        self.x = float(self.rect.x)

    def update (self):
        #Mueve el alien a la derecha o a la izquierda.
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges (self):
        #Devuelve true si el alien llega al límite de la pantalla
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)