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


"""Fases do jogo: em que fase o jogador está, a velocidade de cada fase e o intervalo entre obstáculos."""
import random
from config import VELOCIDADE_INICIAL, AUMENTO_POR_FASE, PONTOS_POR_FASE, FASE_MAXIMA


def calcular_fase(pontos):
    """Retorna a fase atual: sobe 1 a cada PONTOS_POR_FASE pontos, até a FASE_MAXIMA."""
    fase = 1 + pontos // PONTOS_POR_FASE
    if fase > FASE_MAXIMA:
        fase = FASE_MAXIMA
    return fase


def calcular_velocidade(fase):
    """Retorna a velocidade dos obstáculos naquela fase."""
    return VELOCIDADE_INICIAL + (fase - 1) * AUMENTO_POR_FASE


def sortear_intervalo(fase):
    """Sorteia quantos frames esperar até o próximo obstáculo.

    Quanto maior a fase, menor o intervalo (nunca menos de 36 frames,
    para sempre dar tempo de pular e cair).
    """
    menor = max(36, 80 - fase * 5)
    return random.randint(menor, menor + 35)