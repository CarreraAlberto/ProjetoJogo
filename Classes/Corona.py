import pygame 
import random

# Inicia variaveis
larguraw = 1500
largurac = 75
alturac = 75
xlinha = 200

# Classe Corona
class Corona(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1100, larguraw-largurac)
        self.rect.y = random.randint(50, 640-alturac-50)
        self.speedy = random.randint(10, 15)
        self.speedx = random.randint(12, 17) * -1

    def checa(self):
        if self.rect.bottom <= 640-50:
            self.speedy = self.speedy * -1
        if self.rect.top >= 50:
            self.speedy = self.speedy * -1
        if self.rect.left <= xlinha:
            self.speedx = self.speedx * -1

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.checa()
        