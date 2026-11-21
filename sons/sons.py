"""Funções de áudio: efeitos sonoros e música de fundo."""
import os
import pygame
from config import PASTA_SONS


def carregar_sons():
    """Carrega os efeitos sonoros num dicionário. Se um arquivo faltar, o jogo roda sem ele."""
    sons = {}
    for nome in ['pulo', 'fase', 'batida', 'vitoria', 'derrota']:
        caminho = os.path.join(PASTA_SONS, nome + '.wav')
        if os.path.exists(caminho):
            sons[nome] = pygame.mixer.Sound(caminho)
    if 'pulo' in sons:
        sons['pulo'].set_volume(0.4)
    return sons


def tocar(sons, nome):
    """Toca um efeito sonoro, se ele foi carregado."""
    if nome in sons:
        sons[nome].play()


def tocar_musica():
    """Começa a música de fundo em loop (se ela ainda não estiver tocando)."""
    caminho = os.path.join(PASTA_SONS, 'musica.wav')
    if os.path.exists(caminho) and not pygame.mixer.music.get_busy():
        pygame.mixer.stop()                 # corta o som de vitória/derrota, se ainda estiver tocando
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)         # -1 = repetir para sempre


def parar_musica():
    """Para a música de fundo (usado antes dos sons de vitória e derrota)."""
    pygame.mixer.music.stop()
