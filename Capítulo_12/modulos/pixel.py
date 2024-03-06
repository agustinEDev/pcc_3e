import pygame
from pygame.sprite import Sprite

class Pixel(Sprite):
    #Una clase que representa un solo alien en la flota.

    def __init__(self, t):
        #Inicializa el alien y establece su posición inicial.
        super().__init__()
        self.screen = t.screen
        self.speed = t.settings.pixel_speed

        #Carga la imagen del pixel y establece su atributo rect.
        self.image = pygame.image.load('images/pixel.bmp')
        self.rect = self.image.get_rect()

        #Inicia un nuevo pixel cerca de la posición superior izquierda de la pantalla.
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        #Guarda la posición horizontal exacta del pixel.
        self.x = float(self.rect.x)

    def update (self):
        #Mueve el pixel hacia la derecha.
        self.x += self.speed
        self.rect.x = self.x

