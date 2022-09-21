from Classes.Objeto import Objeto

import constantes

class Vacina(Objeto):
    def __init__(self, img, left, centery):
        super().__init__(img)
        self.rect.centery = centery
        self.rect.left = left
        self.speedx = 40

    def checa(self):
        if self.rect.left > constantes.LARGURA_W:
            self.kill()

    def update(self):
        super().update(self.speedx, 0)
        self.checa()