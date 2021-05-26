import pygame
 
pygame.init()

# ----- Gera tela principal 
window = pygame.display.set_mode((1500, 500))
pygame.display.set_caption('Tiro ao alvo')

# ----- Inicia assets 
image_bloco2 = pygame.image.load('imagens/bloco2.png').convert()
image_arqueiro = pygame.image.load('imagens/arqueiro.JPG').convert()
image_arqueiro = pygame.transform.scale(image_arqueiro, (188, 274))
image_alvo = pygame.image.load('imagens/Covid_alvo.png').convert()
image_alvo = pygame.transform.scale(image_alvo, (100, 100))

# ----- Inicia estruturas de dados 
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    
    # ----- Atualiza estado do jogo

    # ----- Gera saídas
    window.fill((255, 255, 255))
    distancia_x = 0
    while distancia_x < 1501:
        window.blit(image_bloco2, (distancia_x, 420))
        distancia_x+=250
    window.blit(image_arqueiro, (0, 145))
    window.blit(image_alvo, (1000, 145))
    pygame.display.update()

# ===== Finalização =====
pygame.quit()