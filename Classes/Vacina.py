import pygame

# Inicia variaveis
larguraw = 1500

# Classe Vacina
class Vacina(pygame.sprite.Sprite):
    def __init__(self, img, left, centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centery = centery
        self.rect.left = left
        self.speedx = 40

    def checa(self):
        if self.rect.left > larguraw:
            self.kill()

    def update(self):
        self.rect.x  += self.speedx
        self.checa()