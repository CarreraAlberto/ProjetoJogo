# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

from Classes import Arco, Corona, Linha
# from Assets import *
import constantes
import funcoes

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((constantes.LARGURA_W, constantes.ALTURA_W))
pygame.display.set_caption('Vacina Corona')

# ----- Inicia assets 
image_bloco2 = pygame.image.load('imagens/bloco2.png').convert()
image_fundo = pygame.image.load('imagens/fundo.png').convert_alpha()
image_fundo = pygame.transform.scale(image_fundo, (1500, 650))
image_arqueiro = pygame.image.load('imagens/arco.png').convert_alpha()
image_arqueiro = pygame.transform.scale(image_arqueiro, (188, 274))
image_alvo = pygame.image.load('imagens/Covid_alvo.png').convert_alpha()
image_alvo = pygame.transform.scale(image_alvo, (constantes.LARGURA_C, constantes.ALTURA_C))
image_linha = pygame.image.load('imagens/linha.png').convert_alpha()
image_linha = pygame.transform.scale(image_linha, (10, 750))
image_vacina = pygame.image.load('imagens/vacina.png').convert_alpha()
image_vacina = pygame.transform.scale(image_vacina, (100, 50))
fonte = pygame.font.SysFont("rockwell", 50)
fonte2 = pygame.font.SysFont("playbill", 50)

todos = pygame.sprite.Group()
agulha = pygame.sprite.Group()
coronaalvo = pygame.sprite.Group()

# bug
pygame.mixer.music.load('imagens/musicajogo.mp3')
pygame.mixer.music.set_volume(0.2)

# ----- Inicia estruturas de dados
arco = Arco.Arco(image_arqueiro, todos, agulha, image_vacina)
todos.add(arco)
 
linha = Linha.Linha(image_linha)
todos.add(linha)

corona = Corona.Corona(image_alvo)
todos.add(corona)
coronaalvo.add(corona)
    
game = True
clock = pygame.time.Clock()
placar = 0
vidas = 3

# ===== Loop principal =====
# bug
pygame.mixer.music.play(loops=-1)
while game:
    clock.tick(constantes.FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        funcoes.movimento_arco(arco, event)
    
    todos.update()
    todos, coronaalvo, placar = funcoes.tiro_acerta_corona(todos, coronaalvo, placar, agulha, image_alvo)
    todos, coronaalvo, placar, game, vidas = funcoes.corona_bate_linha(todos, coronaalvo, placar, linha, image_alvo, game, vidas)

    window = funcoes.gera_saidas(todos, window, image_fundo, image_bloco2)
    window = funcoes.funcao_placar(window, fonte, fonte2, vidas, placar)

    pygame.display.update()  

# ===== Finalização =====
pygame.quit() 
