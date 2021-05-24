import pygame
 
pygame.init()
 
window = pygame.display.set_mode((1500, 500))
pygame.display.set_caption('Tiro ao alvo')
 
game = True

image = pygame.image.load()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
 
    window.fill((255, 255, 255))
    pygame.display.update()
 
pygame.quit()