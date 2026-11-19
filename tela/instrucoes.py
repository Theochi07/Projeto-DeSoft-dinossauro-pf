"""Tela de instruções (tela informativa com os controles e as regras)."""
import pygame
from config import LARGURA, FPS, PRETO, CINZA, PONTOS_POR_FASE, PONTOS_PARA_VENCER, SAIR, MENU
from cenario.cenario import escrever, desenhar_cenario


def tela_instrucoes(janela, fontes):
    """Tela informativa com os controles e as regras. ENTER ou ESC volta ao menu."""
    relogio = pygame.time.Clock()
    while True:
        relogio.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return SAIR
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    return MENU

        desenhar_cenario(janela, 0)
        escrever(janela, fontes['grande'], 'COMO JOGAR', PRETO, LARGURA / 2, 40)
        linhas = [
            'SETA PARA CIMA = pular os cactos',
            'SETA PARA BAIXO = abaixar dos pterodáctilos',
            'P = pausar',
            'Pegue o escudo azul (S): ele aguenta uma batida',
            'A cada ' + str(PONTOS_POR_FASE) + ' pontos o jogo fica mais rápido',
            'Chegue a ' + str(PONTOS_PARA_VENCER) + ' pontos para vencer!',
        ]
        y = 90
        for linha in linhas:
            escrever(janela, fontes['normal'], linha, CINZA, LARGURA / 2, y)
            y = y + 28
        escrever(janela, fontes['normal'], 'ENTER ou ESC = voltar', PRETO, LARGURA / 2, 275)
        pygame.display.update()
