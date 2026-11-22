"""Tela de vitória (quando o jogador chega na meta de pontos)."""
import pygame
from config import LARGURA, FPS, PRETO, CINZA, VERDE, SAIR, MENU, JOGANDO
from personagem.dino import criar_dino, desenhar_dino
from cenario.cenario import escrever, desenhar_cenario, desenhar_chao
from sons.sons import tocar, parar_musica


def tela_vitoria(janela, fontes, sons, imagens, pontos):
    """Tela de quem chegou na meta, com som de vitória. ENTER joga de novo, ESC volta ao menu."""
    relogio = pygame.time.Clock()
    parar_musica()
    tocar(sons, 'vitoria')
    while True:
        relogio.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return SAIR
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return JOGANDO
                if event.key == pygame.K_ESCAPE:
                    return MENU

        desenhar_cenario(janela, 0)
        escrever(janela, fontes['grande'], 'VOCÊ VENCEU!', VERDE, LARGURA / 2, 70)
        escrever(janela, fontes['normal'], 'Você chegou a ' + str(pontos) + ' pontos!', CINZA, LARGURA / 2, 135)
        escrever(janela, fontes['normal'], 'ENTER = jogar de novo  |  ESC = menu', PRETO, LARGURA / 2, 200)
        desenhar_dino(janela, criar_dino(), 0, imagens)
        desenhar_chao(janela, 0)
        pygame.display.update()
