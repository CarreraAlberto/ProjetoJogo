import pygame

# Inicia variaveis
xlinha = 200

# Classe Linha
class Linha(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.left = xlinha
        self.rect.top = -100
