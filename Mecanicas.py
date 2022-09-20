# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from Classes import Arco, Corona, Linha

pygame.init()
pygame.mixer.init()
# ----- Gera tela principal
tempofps = 0
larguraw = 1500
alturaw = 750
largurac = 75
alturac = 75
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
image_vacina = pygame.transform.scale(image_vacina, (100, 50))
fonte = pygame.font.SysFont("rockwell", 50)
fonte2 = pygame.font.SysFont("playbill", 50)

todos = pygame.sprite.Group()
agulha = pygame.sprite.Group()
coronaalvo = pygame.sprite.Group()

# pygame.mixer.music.load('imagens/musicajogo.mp3')
# pygame.mixer.music.set_volume(0.2)

# ----- Inicia estruturas de dados
#Define tipo arqueiro
arco = Arco.Arco(image_arqueiro, todos, agulha, image_vacina)
todos.add(arco)
 
#Criando linha
linha = Linha.Linha(image_linha)
todos.add(linha)

#Cria o corona
corona = Corona.Corona(image_alvo)
todos.add(corona)
coronaalvo.add(corona)
    
# Jogo
game = True
# FPS do jogo
clock = pygame.time.Clock()
FPS = 15

#Placar
placar = 0
#Vidas
vidas = 3
# ===== Loop principal =====
# pygame.mixer.music.play(loops=-1)
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

    # ----- Atualiza estado do jogo
    todos.update()

    # Tiro acerta corona
    colisao = pygame.sprite.groupcollide(coronaalvo, agulha, True, True)
    for corona in colisao:
        c = Corona.Corona(image_alvo)
        todos.add(c)
        coronaalvo.add(c)
        placar +=10

    # Corona bate na linha
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

    # ----- Gera saídas
    window.fill((255, 255, 255))
    distancia_x = 0
    
    window.blit(image_fundo, (0,0))
    while distancia_x < 1501:
        window.blit(image_bloco2, (distancia_x, 650))
        distancia_x+=250
    todos.draw(window)
    
    #Placar
    oplacar = fonte.render("{:08d}".format(placar), True, (255, 255, 255))
    aparecerp = oplacar.get_rect()
    aparecerp.midtop = (larguraw/2 + 250, 10)
    window.blit(oplacar, aparecerp)

    asvidas = fonte2.render("Vidas: {0} ".format(vidas), True, (255, 255, 255))
    aparecerv = asvidas.get_rect()
    aparecerv.midtop = (150, 10)
    window.blit(asvidas, aparecerv)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
