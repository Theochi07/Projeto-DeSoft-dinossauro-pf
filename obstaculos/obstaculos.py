"""Obstáculos (cactos e pterodáctilos) e o escudo: criar e desenhar.

Cada obstáculo é um dicionário; todos ficam juntos numa lista.
O movimento e a colisão ficam na pasta mecanica/.
"""
import random
import pygame
from config import LARGURA, CHAO, VERDE, CINZA, AZUL


def criar_obstaculo(fase):
    """Sorteia um obstáculo. Pterodáctilos só aparecem a partir da fase 2."""
    if fase == 1:
        tipo = random.choice(['cacto', 'cacto_grande'])
    else:
        tipo = random.choice(['cacto', 'cacto_grande', 'ptero'])

    if tipo == 'cacto':
        return {
            'tipo': tipo,
            'x': LARGURA,
            'y': CHAO - 48,
            'largura': 20,
            'altura': 48
        }

    elif tipo == 'cacto_grande':
        return {
            'tipo': tipo,
            'x': LARGURA,
            'y': CHAO - 58,
            'largura': 34,
            'altura': 58
        }

    else:
        # O ptero voa na altura da cabeça: em pé bate, abaixado passa por baixo
        return {
            'tipo': tipo,
            'x': LARGURA,
            'y': CHAO - 60,
            'largura': 46,
            'altura': 30
        }


def desenhar_obstaculo(janela, obs, frames):
    """Desenha um cacto (verde) ou um pterodáctilo (com asas batendo)."""
    x = obs['x']
    y = obs['y']

    if obs['tipo'] == 'ptero':
        pygame.draw.rect(
            janela, CINZA, (x + 6, y + 12, 34, 6)
        )  # corpo

        pygame.draw.polygon(
            janela,
            CINZA,
            [(x + 40, y + 12), (x + 46, y + 15), (x + 40, y + 18)]
        )  # bico

        if (frames // 10) % 2 == 0:   # asas para cima
            pygame.draw.polygon(
                janela,
                CINZA,
                [(x + 14, y + 13), (x + 24, y), (x + 28, y + 13)]
            )
        else:                         # asas para baixo
            pygame.draw.polygon(
                janela,
                CINZA,
                [(x + 14, y + 17), (x + 24, y + 29), (x + 28, y + 17)]
            )

    else:
        meio = x + obs['largura'] // 2

        pygame.draw.rect(
            janela, VERDE, (meio - 5, y, 10, obs['altura'])
        )  # tronco

        pygame.draw.rect(
            janela, VERDE, (x, y + 14, 6, 14)
        )  # braço esquerdo

        pygame.draw.rect(
            janela, VERDE, (x, y + 24, obs['largura'] // 2, 5)
        )

        pygame.draw.rect(
            janela, VERDE, (x + obs['largura'] - 6, y + 8, 6, 14)
        )  # braço direito

        pygame.draw.rect(
            janela, VERDE, (meio, y + 18, obs['largura'] // 2, 5)
        )


def criar_escudo():
    """Cria o power-up de escudo na direita da tela, um pouco acima do chão."""
    return {
        'x': LARGURA,
        'y': CHAO - 36,
        'largura': 26,
        'altura': 26
    }


def desenhar_escudo(janela, escudo, fonte):
    """Desenha o escudo: um círculo azul com a letra S."""
    centro = (escudo['x'] + 13, escudo['y'] + 13)
    pygame.draw.circle(janela, AZUL, centro, 13)

    letra = fonte.render('S', True, (255, 255, 255))
    janela.blit(letra, letra.get_rect(center=centro))