import pygame

class Comecocos:
    #Clase para gestionar el comecocos

    def __init__ (self, va):
        self.screen = va.pantalla
        self.screen_rect = va.pantalla.get_rect()
        #carga la imagen del comecocos y obtiene su rect
        self.image = pygame.image.load('images/pixel.bmp')
        self.rect = self.image.get_rect()
        #coloca el comecocos en el centro
        self.rect.center = self.screen_rect.center

    def blitme(self):
        #Dibuja la nave en su posición actual
        self.screen.blit(self.image, self.rect)

