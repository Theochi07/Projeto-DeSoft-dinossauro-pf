"""Desenhos do cenário e do texto: céu, sol, nuvens, chão e escrita na tela."""
import pygame
from config import LARGURA, CHAO, CEU, CINZA, CINZA_CLARO, AMARELO, BRANCO


def escrever(janela, fonte, texto, cor, x, y):
    """Escreve um texto centralizado no ponto (x, y)."""
    imagem = fonte.render(texto, True, cor)
    retangulo = imagem.get_rect(center=(x, y))
    janela.blit(imagem, retangulo)


def desenhar_cenario(janela, deslocamento):
    """Pinta o céu, o sol e 3 nuvens que andam devagar (mais devagar que o chão)."""
    janela.fill(CEU)
    pygame.draw.circle(janela, AMARELO, (LARGURA - 90, 60), 28)   # sol
    for i in range(3):
        # As nuvens andam a 20% da velocidade do chão e voltam pela direita ao sair da tela
        x = (i * 330 - deslocamento * 0.2) % (LARGURA + 120) - 60
        y = 50 + i * 35
        pygame.draw.ellipse(janela, BRANCO, (x, y, 70, 22))
        pygame.draw.ellipse(janela, BRANCO, (x + 20, y - 10, 40, 24))


def desenhar_chao(janela, deslocamento):
    """Desenha o chão com tracinhos que andam (dá ideia de movimento)."""
    pygame.draw.line(janela, CINZA, (0, CHAO), (LARGURA, CHAO), 2)
    x = -(deslocamento % 40)
    while x < LARGURA:
        pygame.draw.line(janela, CINZA_CLARO, (x, CHAO + 8), (x + 10, CHAO + 8), 2)
        x = x + 40


"""Colisão: verifica se dois objetos do jogo (dicionários com x, y, largura e altura) se encostam."""
import pygame


def bateu(a, b):
    """Retorna True se os retângulos de 'a' e 'b' se encostam.

    Os retângulos são um pouco menores que o desenho, para o jogo
    não contar batida quando só a pontinha encostou.
    """
    ret_a = pygame.Rect(a['x'] + 4, a['y'] + 4, a['largura'] - 8, a['altura'] - 6)
    ret_b = pygame.Rect(b['x'] + 3, b['y'] + 3, b['largura'] - 6, b['altura'] - 6)
    return ret_a.colliderect(ret_b)