import pygame

from Classes.Objeto import Objeto
from Classes.Vacina import Vacina
import constantes

class Arco(Objeto):
    def __init__(self,img,todos,agulha, image_vacina):
        super().__init__(img)
        self.rect.centery = constantes.ALTURA_W / 2
        self.rect.left = 0
        self.speedy = 0
        self.todos = todos
        self.agulha = agulha
        self.image_vacina = image_vacina
        self.last_shot = pygame.time.get_ticks()
        self.vacinar_ticks = 1000

    def checa(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 650:
            self.rect.bottom = 650

    def update(self):
        super().update(0, self.speedy)
        self.checa()

    def vacinar(self):
        tiro = pygame.time.get_ticks()
        elapsed_ticks = tiro - self.last_shot

        if elapsed_ticks > self.vacinar_ticks:
            self.last_shot = tiro
            vacina0 = Vacina(self.image_vacina,150,self.rect.centery-30)
            self.agulha.add(vacina0)
            self.todos.add(vacina0)
