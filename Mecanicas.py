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
game = True
corona_x = random.randint(500, larguraw-largurac)
corona_y = random.randint(0+75, 550-alturac-75)
corona_y0 = corona_y
coronaspeed_y = random.randint(1, 5)
clock = pygame.time.Clock()
FPS = 15

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    
    # Atualizando a posição do meteoro:
    corona_y += coronaspeed_y

    # Fazer o corona ir e voltar 
    tempofps +=1
    if tempofps > 150:
        corona_x = random.randint(500, larguraw-largurac)
        corona_y = random.randint(0+75, 550-alturac-75)
        corona_y0 = corona_y
        coronaspeed_y = random.randint(1, 5)
        tempofps = 0
    
    if corona_y > corona_y0+75:
        coronaspeed_y = coronaspeed_y*-1
    if corona_y < corona_y0-75:
        coronaspeed_y = coronaspeed_y*-1

    # ----- Gera saídas
    window.fill((255, 255, 255))
    distancia_x = 0
    while distancia_x < 1501:
        window.blit(image_bloco2, (distancia_x, 650))
        distancia_x+=250
    window.blit(image_arqueiro, (0, 200))
    window.blit(image_alvo, (corona_x, corona_y))
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados