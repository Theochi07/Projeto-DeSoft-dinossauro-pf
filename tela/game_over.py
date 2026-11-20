"""Tela de game over (fim de jogo quando o dino bate)."""
import pygame
from config import LARGURA, FPS, PRETO, CINZA, AZUL, SAIR, MENU, JOGANDO
from cenario.cenario import escrever, desenhar_cenario, desenhar_chao
from sons.sons import tocar, parar_musica


def tela_game_over(janela, fontes, sons, pontos, recorde):
    """Mostra os pontos e toca o som de derrota. ENTER joga de novo, ESC volta ao menu."""
    relogio = pygame.time.Clock()
    parar_musica()
    tocar(sons, 'derrota')
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
        escrever(janela, fontes['grande'], 'GAME OVER', PRETO, LARGURA / 2, 70)
        escrever(janela, fontes['normal'], 'Pontos: ' + str(pontos), CINZA, LARGURA / 2, 130)
        escrever(janela, fontes['normal'], 'Recorde: ' + str(recorde), AZUL, LARGURA / 2, 162)
        escrever(janela, fontes['normal'], 'ENTER = jogar de novo  |  ESC = menu', PRETO, LARGURA / 2, 205)
        desenhar_chao(janela, 0)
        pygame.display.update()
