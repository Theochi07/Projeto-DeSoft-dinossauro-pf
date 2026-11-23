"""Fases do jogo: em que fase o jogador está, a velocidade de cada fase e o intervalo entre obstáculos."""
import random
from config import (
    VELOCIDADE_INICIAL,
    AUMENTO_POR_FASE,
    PONTOS_POR_FASE,
    FASE_MAXIMA
)


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