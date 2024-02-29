import pygame

class Gargola:
    #Clase para gestionar la gárgola

    def __init__ (self, jg):
        self.screen = jg.screen
        self.screen_rect = jg.screen.get_rect()
        #Carga la imagen de la gárgola y obtiene su rect
        self.image = pygame.image.load('images/gargoyle.bmp')
        self.rect = self.image.get_rect()
        self.speed = 1.5
        #coloca la gárgola en el centro
        self.rect.midright = self.screen_rect.midright

        #Guarda un valor decimal para la posición horizontal exacta de la gárgola
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Banderas de movimiento; empiezan sin movimiento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme (self):
        #Dibuja la gárgola en su posición actual
        self.screen.blit(self.image, self.rect)

    def update (self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        elif self.moving_left and self.rect.x > self.screen_rect.left:
            self.x -= self.speed
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.speed
        elif self.moving_down and self.rect.y < self.screen_rect.bottom - self.rect.height:
            self.y += self.speed

        #Actualiza el objeto rect de self.x
        self.rect.x = self.x
        #Actualiza el objeto rect de self.y
        self.rect.y = self.y
