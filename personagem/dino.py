"""O personagem: criar o dinossauro, carregar a imagem dele e desenhar na tela.

O dinossauro é um dicionário com a posição, o tamanho e o estado dele.
O movimento (pulo e gravidade) fica em mecanica/movimento.py.
"""
import os
import pygame
from config import CHAO, AZUL


def criar_dino():
    """Cria o dinossauro como um dicionário, parado no chão."""
    dino = {
        'x': 60,             # o dino nunca anda para os lados: quem anda são os obstáculos
        'y': CHAO - 48,
        'largura': 44,
        'altura': 48,
        'vel_y': 0,          # velocidade vertical
        'no_chao': True,
        'abaixado': False,
        'escudo': False,     # True quando ele pegou o power-up
    }
    return dino


def carregar_imagens_dino():
    """Carrega a imagem do personagem (personagem/personagem.png) em dois tamanhos: em pé e abaixado.

    Para trocar o personagem, basta trocar esse arquivo por outro PNG com fundo transparente.
    """
    pasta_personagem = os.path.dirname(os.path.abspath(__file__))
    caminho_imagem = os.path.join(pasta_personagem, 'personagem.png')

    imagem = pygame.image.load(caminho_imagem).convert_alpha()

    imagens = {
        'em_pe': pygame.transform.scale(imagem, (44, 48)),
        'abaixado': pygame.transform.scale(imagem, (58, 26)),   # achatado ao abaixar
    }
    return imagens


def desenhar_dino(janela, dino, frames, imagens):
    """Desenha a imagem do personagem. Correndo no chão, ele dá pulinhos de 2 pixels (animação)."""
    pulinho = 0

    if dino['no_chao'] and (frames // 6) % 2 == 1:
        pulinho = 2

    if dino['abaixado']:
        janela.blit(
            imagens['abaixado'],
            (dino['x'], dino['y'] - pulinho)
        )
    else:
        janela.blit(
            imagens['em_pe'],
            (dino['x'], dino['y'] - pulinho)
        )

    # Se tem escudo, desenha um círculo azul em volta
    if dino['escudo']:
        centro = (
            dino['x'] + dino['largura'] // 2,
            dino['y'] + dino['altura'] // 2
        )
        pygame.draw.circle(janela, AZUL, centro, 36, 2)