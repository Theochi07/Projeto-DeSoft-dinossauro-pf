"""Tela de menu (início do jogo)."""
import pygame
from config import LARGURA, FPS, PRETO, CINZA, AZUL, PONTOS_PARA_VENCER, SAIR, INSTRUCOES, JOGANDO
from personagem.dino import criar_dino, desenhar_dino
from cenario.cenario import escrever, desenhar_cenario, desenhar_chao
from sons.sons import tocar_musica


def tela_menu(janela, fontes, imagens, recorde):
    """Tela inicial. ENTER começa, I abre as instruções, ESC sai."""
    relogio = pygame.time.Clock()
    tocar_musica()
    while True:
        relogio.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return SAIR
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return JOGANDO
                if event.key == pygame.K_i:
                    return INSTRUCOES
                if event.key == pygame.K_ESCAPE:
                    return SAIR

        desenhar_cenario(janela, 0)
        escrever(janela, fontes['grande'], 'DINO RUSH', PRETO, LARGURA / 2, 60)
        escrever(janela, fontes['normal'], 'Meta: ' + str(PONTOS_PARA_VENCER) + ' pontos   |   Recorde: ' + str(recorde),
                 AZUL, LARGURA / 2, 120)
        escrever(janela, fontes['normal'], 'ENTER = jogar', PRETO, LARGURA / 2, 160)
        escrever(janela, fontes['normal'], 'I = instruções   |   ESC = sair', CINZA, LARGURA / 2, 192)
        desenhar_dino(janela, criar_dino(), 0, imagens)
        desenhar_chao(janela, 0)
        pygame.display.update()
