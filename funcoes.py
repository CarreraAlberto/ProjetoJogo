import pygame

from Classes import Corona
import constantes

# def trata_eventos(events, game, arco):
#     event = events[0]
#     for event in events:
#         # ----- Verifica consequências
#         if event.type == pygame.QUIT:
#             game = False

#     movimento_arco(arco, event)
#     return game

def movimento_arco(arco, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            arco.speedy -= 20
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            arco.speedy += 20
        if event.key == pygame.K_SPACE or event.key == pygame.K_q:
            arco.vacinar()
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            arco.speedy += 20
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            arco.speedy -= 20

def tiro_acerta_corona(todos, coronaalvo, placar, agulha, image_alvo):
        colisao = pygame.sprite.groupcollide(coronaalvo, agulha, True, True)
        for corona in colisao:
            c = Corona.Corona(image_alvo)
            todos.add(c)
            coronaalvo.add(c)
            placar +=10
        
        return todos, coronaalvo, placar

def corona_bate_linha(todos, coronaalvo, placar, linha, image_alvo, game, vidas): 
    colisao = pygame.sprite.spritecollide(linha,coronaalvo,True) 
    if len(colisao)>0:
        vidas -= 1
        if vidas == 0:
            game = False
        else:
            game = True
            for corona in colisao:
                c = Corona.Corona(image_alvo)
                todos.add(c)
                coronaalvo.add(c)
                placar -=100
    
    return todos, coronaalvo, placar, game, vidas

def gera_saidas(todos, window, image_fundo, image_bloco2):
    window.fill((255, 255, 255))
    distancia_x = 0
    window.blit(image_fundo, (0,0))
    while distancia_x < 1501:
        window.blit(image_bloco2, (distancia_x, 650))
        distancia_x+=250
    todos.draw(window)

    return window

def funcao_placar(window, fonte, fonte2, vidas, placar):
    oplacar = fonte.render("{:08d}".format(placar), True, (255, 255, 255))
    aparecerp = oplacar.get_rect()
    aparecerp.midtop = (constantes.LARGURA_W/2 + 250, 10)
    window.blit(oplacar, aparecerp)

    asvidas = fonte2.render("Vidas: {0} ".format(vidas), True, (255, 255, 255))
    aparecerv = asvidas.get_rect()
    aparecerv.midtop = (150, 10)
    window.blit(asvidas, aparecerv)

    return window
