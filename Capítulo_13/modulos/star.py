import pygame
from random import randint


class Star:

    def __init__(self, fs):
        #Inicializa Star con los valores de la pantalla
        self.screen = fs.screen
        self.screen_rect = fs.screen.get_rect()
        #Carga la imagen y obtiene su rect
        self.image = pygame.image.load('images/star.bmp')
        self.image_2 = pygame.image.load('images/metal_star.bmp')
        self.rect = self.image.get_rect()
        #Posiciona la imagen inicialmente en el centro de la pantalla
        self.rect.center = self.screen_rect.center

        #Guarda las coordinadas de la imagen como floats
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme (self, i):
        for a in range(10000):
            #Dibuja la imagen en la pantalla
            current_x = self.x - self.image.get_width()
            current_y = self.y - self.image.get_height()
            current_rect = current_x, current_y
            #Arriba izquierda
            if i == 0:
                self.screen.blit(self.image_2, current_rect)
            else:
                self.screen.blit(self.image, current_rect)
            current_rect = current_x + 2 * self.image.get_width(), current_y
            #Arriba derecha
            if i == 1:
                self.screen.blit(self.image_2, current_rect)
            else:
                self.screen.blit(self.image, current_rect)
            current_rect = current_x, current_y + 2 * self.image.get_height()
            #Abajo izquierda
            if i == 3:
                self.screen.blit(self.image_2, current_rect)
            else:
                self.screen.blit(self.image, current_rect)
            current_x = current_x + 2 * self.image.get_width()
            current_y = current_y + 2 * self.image.get_height()
            current_rect = current_x, current_y
            #Abajo derecha
            if i == 2:
                self.screen.blit(self.image_2, current_rect)
            else:
                self.screen.blit(self.image, current_rect)
