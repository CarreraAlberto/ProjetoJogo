import random

from Classes.Objeto import Objeto
import constantes

class Corona(Objeto):
    def __init__(self, img):
        super().__init__(img)
        self.rect.x = random.randint(1100, constantes.LARGURA_W-constantes.LARGURA_C)
        self.rect.y = random.randint(50, 640-constantes.ALTURA_C-50)
        self.speedy = random.randint(10, 15)
        self.speedx = random.randint(12, 17) * -1

    def checa(self):
        if self.rect.bottom <= 640-50:
            self.speedy = self.speedy * -1
        if self.rect.top >= 50:
            self.speedy = self.speedy * -1
        if self.rect.left <= constantes.X_LINHA:
            self.speedx = self.speedx * -1

    def update(self):
        super().update(self.speedx, self.speedy)
        self.checa()
