import pygame
 
pygame.init()
 
window = pygame.display.set_mode((1500, 500))
pygame.display.set_caption('Tiro ao alvo')
 
game = True

image = pygame.image.load('imagens/bloco2.png').convert()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
 
    window.fill((255, 255, 255))
    distancia_x = 0
    while distancia_x < 1501:
        window.blit(image, (distancia_x, 420))
        distancia_x+=250
    pygame.display.update()

pygame.quit()