import pygame

import constantes

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