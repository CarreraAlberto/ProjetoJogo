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
window = pygame.display.set_mode((larguraw, alturaw))
pygame.display.set_caption('Libere a Badernahhh')
 
# ----- Inicia assets 
image_bloco2 = pygame.image.load('imagens/bloco2.png').convert()
image_arqueiro = pygame.image.load('imagens/arco.png').convert()
image_arqueiro = pygame.transform.scale(image_arqueiro, (188, 274))
image_alvo = pygame.image.load('imagens/Covid_alvo.png').convert()
image_alvo = pygame.transform.scale(image_alvo, (largurac, alturac))

# ----- Inicia estruturas de dados
# Defini tipo corona
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

        if self.rect.bottom <= 640:
            self.speedy = self.speedy * -1
        if self.rect.top >= 10:
            self.speedy = self.speedy * -1
        if self.rect.left <= 250:
            self.speedx = self.speedx * -1
        if self.rect.right >= 1490:
            self.speedx = self.speedx * -1


game = True
# FPS do jogo
clock = pygame.time.Clock()
FPS = 15

#Cria o corona
corona = Corona(image_alvo)

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    corona.update()

    # Fazer o corona ir e voltar 
    
    # ----- Gera saídas
    window.fill((255, 255, 255))
    distancia_x = 0
    while distancia_x < 1501:
        window.blit(image_bloco2, (distancia_x, 650))
        distancia_x+=250
    window.blit(image_arqueiro, (0, 200))
    window.blit(corona.image, corona.rect)
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados