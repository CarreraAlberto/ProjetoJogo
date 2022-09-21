import pygame

import constantes

class Linha(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.left = constantes.X_LINHA
        self.rect.top = -100
