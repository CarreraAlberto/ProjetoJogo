import pygame
import random
 
pygame.init()
 
# ----- Gera tela principal
larguraw = 1500
alturaw = 800
largurac = 100
alturac = 100
window = pygame.display.set_mode((larguraw, alturaw))
pygame.display.set_caption('Libere a Badernahhh')
 
# ----- Inicia assets 
image_bloco2 = pygame.image.load('imagens/bloco2.png').convert()
image_arqueiro = pygame.image.load('imagens/arco.png').convert()
image_arqueiro = pygame.transform.scale(image_arqueiro, (188, 274))
image_alvo = pygame.image.load('imagens/Covid_alvo.png').convert()
image_alvo = pygame.transform.scale(image_alvo, (100, 100))
 
# ----- Inicia estruturas de dados 
# Definindo os novos tipos
class arqueiro(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
 
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = larguraw / 2
        self.rect.bottom = alturaw
        self.speedx = 0
 
    def update(self):
        # Atualização da posição do arco
        self.rect.x += self.speedx
 
        # Não deixa sair da tela
        if self.rect.right > alturaw:
            self.rect.right = alturaw
        if self.rect.left < 0:
            self.rect.left = 0
 
class virus(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
 
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(500, larguraw-largurac)
        self.rect.y = random.randint(0, 650)
 
    def update(self):
        # Atualizando a posição do meteoro
 
        # Se o tempo de 7 segundos acabar, sorteia nova posição do covid
        if 1<0:
            self.rect.x = random.randint(500, larguraw-largurac)
            self.rect.y = random.randint(0, 650)
 
game = True
 
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30
 
# Criando covid
sprite = pygame.sprite.Group()
# Criando jogador
player = arqueiro(image_arqueiro)
sprite.add(player)
#Criando o Covid
Covid = virus(image_alvo)
sprite.add(virus)
 
# ===== Loop principal =====
while game:
    clock.tick(FPS)
 
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
 
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_UP:
                player.speedx -= 8
            if event.key == pygame.K_DOWN:
                player.speedx += 8
 
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.speedx += 8
            if event.key == pygame.K_DOWN:
                player.speedx -= 8
 
    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    sprite.update()
 
    # ----- Gera saídas
    window.fill((255, 255, 255))
    distancia_x = 0
    while distancia_x < 1501:
        window.blit(image_bloco2, (distancia_x, 700))
        distancia_x+=250
    window.blit(image_arqueiro, (0, 145))
    window.blit(image_alvo, (1000, 145))
    sprite.draw(window)
    
    pygame.display.update()
 
# ===== Finalização =====
pygame.quit()