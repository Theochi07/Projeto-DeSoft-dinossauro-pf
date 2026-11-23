"""Colisão: verifica se dois objetos do jogo (dicionários com x, y, largura e altura) se encostam."""
import pygame


def bateu(a, b):
    """Retorna True se os retângulos de 'a' e 'b' se encostam.

    Os retângulos são um pouco menores que o desenho, para o jogo
    não contar batida quando só a pontinha encostou.
    """
    ret_a = pygame.Rect(
        a['x'] + 4,
        a['y'] + 4,
        a['largura'] - 8,
        a['altura'] - 6
    )
    ret_b = pygame.Rect(
        b['x'] + 3,
        b['y'] + 3,
        b['largura'] - 6,
        b['altura'] - 6
    )
    return ret_a.colliderect(ret_b)