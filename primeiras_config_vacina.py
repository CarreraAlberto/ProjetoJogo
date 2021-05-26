import pygame
 
pygame.init()

# ----- Gera tela principal
larguraw = 1500
alturaw = 800
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
        # Atualização da posição da mira
        self.rect.x += self.speedx

        if self.rect.right > alturaw:
            self.rect.right = alturaw
        if self.rect.left < 0:
            self.rect.left = 0



game = True

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando jogador
player = arqueiro(image_arqueiro)
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

    # ----- Atualiza estado do jogo
    # ----- Gera saídas
    window.fill((255, 255, 255))
    distancia_x = 0
    while distancia_x < 1501:
        window.blit(image_bloco2, (distancia_x, 700))
        distancia_x+=250
    window.blit(image_arqueiro, (0, 145))
    window.blit(image_alvo, (1000, 145))
    pygame.display.update()

# ===== Finalização =====
pygame.quit()