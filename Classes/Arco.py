import pygame
from Classes.Vacina import Vacina

# Inicia variaveis
alturaw = 750

# Classe Arco
class Arco(pygame.sprite.Sprite):
    def __init__(self,img,todos,agulha, image_vacina):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centery = alturaw / 2
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
        self.rect.y += self.speedy
        self.checa()

    # Cria a vacina
    def vacinar(self):
        #Pode atirar?
        tiro = pygame.time.get_ticks()
        elapsed_ticks = tiro - self.last_shot

        if elapsed_ticks > self.vacinar_ticks:
            self.last_shot = tiro
            vacina0 = Vacina(self.image_vacina,150,self.rect.centery-30)
            self.agulha.add(vacina0)
            self.todos.add(vacina0)