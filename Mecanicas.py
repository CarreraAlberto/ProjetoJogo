# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
tempofps = 0
larguraw = 1500
alturaw = 750
largurac = 100
alturac = 100
xlinha = 200
window = pygame.display.set_mode((larguraw, alturaw))
pygame.display.set_caption('Libere a Badernahhh')
 
# ----- Inicia assets 
image_bloco2 = pygame.image.load('imagens/bloco2.png').convert()
image_fundo = pygame.image.load('imagens/fundo.png').convert_alpha()
image_fundo = pygame.transform.scale(image_fundo, (1500, 650))
image_arqueiro = pygame.image.load('imagens/arco.png').convert_alpha()
image_arqueiro = pygame.transform.scale(image_arqueiro, (188, 274))
image_alvo = pygame.image.load('imagens/Covid_alvo.png').convert_alpha()
image_alvo = pygame.transform.scale(image_alvo, (largurac, alturac))
image_linha = pygame.image.load('imagens/linha.png').convert_alpha()
image_linha = pygame.transform.scale(image_linha, (10, 750))
image_vacina = pygame.image.load('imagens/vacina.png').convert_alpha()
image_vacina = pygame.transform.scale(image_vacina, (150, 75))

# ----- Inicia estruturas de dados
#Define tipo arqueiro
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

    def update(self):
        self.rect.y += self.speedy

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 650:
            self.rect.bottom = 650

    # Cria a vacina
    def vacinar(self):
        vacina0 = Vacina(self.image_vacina,xlinha+20,self.rect.centery)
        self.agulha.add(vacina0)
        self.todos.add(vacina0)

#Define linha
class Linha(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.left = xlinha
        self.rect.top = -100

#Define tipo corona
class Corona(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1100, larguraw-largurac)
        self.rect.y = random.randint(50, 640-alturac-50)
        self.speedy = random.randint(7, 10)
        self.speedx = random.randint(5,10) * -1

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.bottom <= 640-50:
            self.speedy = self.speedy * -1
        if self.rect.top >= 10:
            self.speedy = self.speedy * -1
        if self.rect.left <= xlinha:
            self.speedx = self.speedx * -1
    
#Define a vacina
class Vacina(pygame.sprite.Sprite):
    def __init__(self, img, left, centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centery = centery
        self.rect.left = left
        self.speedx = 25

    def update(self):
        self.rect.x  += self.speedx
        if self.rect.left > larguraw:
            self.kill()


game = True
# FPS do jogo
clock = pygame.time.Clock()
FPS = 15

#Cria o corona
todos = pygame.sprite.Group()
corona = Corona(image_alvo)
todos.add(corona)
coronaalvo = pygame.sprite.Group()
coronaalvo.add(corona)
agulha = pygame.sprite.Group()
#Criando o player
arco = Arco(image_arqueiro, todos, agulha, image_vacina)
todos.add(arco)
#Criando linha
linha = Linha(image_linha)
todos.add(linha)

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        # Faz o arco andar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                arco.speedy -= 12
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                arco.speedy += 12
            if event.key == pygame.K_SPACE or event.key == pygame.K_q:
                arco.vacinar()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                arco.speedy += 12
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                arco.speedy -= 12

    # ----- Atualiza estado do jogo
    todos.update()

    # Corona bate na linha
    colisao = pygame.sprite.spritecollide(linha,coronaalvo,True) 
    if len(colisao)>0:
        game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))
    distancia_x = 0
    
    window.blit(image_fundo, (0,0))
    while distancia_x < 1501:
        window.blit(image_bloco2, (distancia_x, 650))
        distancia_x+=250
    todos.draw(window)
    
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados