import pygame
 
pygame.init()
 
window = pygame.display.set_mode((1500, 500))
pygame.display.set_caption('Tiro ao alvo')
 
game = True

image_bloco = pygame.image.load('imagens/bloco.png').convert()
image_arqueiro = pygame.image.load('imagens/arqueiro.JPG').convert()
image_arqueiro = pygame.transform.scale(image_arqueiro, (188, 274))

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
 
    window.fill((255, 255, 255))
    distancia_x = 0
    while distancia_x < 1501:
        window.blit(image_bloco, (distancia_x, 420))
        distancia_x+=250
    window.blit(image_arqueiro, (0, 0))
    pygame.display.update()
 
pygame.quit()