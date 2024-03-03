import pygame
import sys

class Gota():

    def __init__ (self, lluvia):
        self.screen = lluvia.screen
        self.screen_rect = lluvia.screen.get_rect()
        self.velocidad = 3.0

        self.image = pygame.image.load('images/gota.bmp')
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height
        self.rect.midtop = self.screen_rect.midtop
        self.y = float(self.rect.y)

    def update (self):
        self.y += self.velocidad
        self.rect.y = self.y

    def reset (self):
        self.y = 0
        self.rect.y = self.y

    def blitme (self):
        self.rect.y = self.y - self.rect.height
        self.screen.blit(self.image, self.rect)
