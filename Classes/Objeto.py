import pygame

class Objeto(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()

    def update(self, speedx, speedy):
        self.rect.y += speedy
        self.rect.x += speedx
