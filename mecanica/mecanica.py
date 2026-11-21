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

"""Movimento do jogo: o pulo e a gravidade do dino e o avanço dos obstáculos."""
from config import CHAO, GRAVIDADE, FORCA_PULO


def pular(dino):
    """Faz o dino pular, só se estiver no chão. Retorna True se pulou."""
    if dino['no_chao'] and not dino['abaixado']:
        dino['vel_y'] = FORCA_PULO
        dino['no_chao'] = False
        return True
    return False


def atualizar_dino(dino, segurando_baixo):
    """Aplica a gravidade e muda o tamanho do dino quando ele abaixa."""
    # Gravidade: a velocidade aumenta e o dino cai
    dino['vel_y'] = dino['vel_y'] + GRAVIDADE
    dino['y'] = dino['y'] + dino['vel_y']

    # Guarda onde estão os pés ANTES de mudar a altura.
    # Assim, ao abaixar, ele encolhe para baixo e continua com os pés no chão.
    pes = dino['y'] + dino['altura']

    # Abaixado ele fica mais baixo e mais comprido (só pode abaixar no chão)
    dino['abaixado'] = segurando_baixo and dino['no_chao']
    if dino['abaixado']:
        dino['largura'] = 58
        dino['altura'] = 26
    else:
        dino['largura'] = 44
        dino['altura'] = 48
    dino['y'] = pes - dino['altura']

    # Se encostou no chão, para de cair
    if dino['y'] + dino['altura'] >= CHAO:
        dino['y'] = CHAO - dino['altura']
        dino['vel_y'] = 0
        dino['no_chao'] = True


def mover_obstaculos(obstaculos, velocidade):
    """Move todos para a esquerda e devolve só os que ainda estão na tela."""
    na_tela = []
    for obs in obstaculos:
        obs['x'] = obs['x'] - velocidade
        if obs['x'] + obs['largura'] > 0:
            na_tela.append(obs)
    return na_tela