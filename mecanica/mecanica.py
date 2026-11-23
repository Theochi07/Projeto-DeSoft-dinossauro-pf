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

"""O personagem: criar o dinossauro, carregar a imagem dele e desenhar na tela.

O dinossauro é um dicionário com a posição, o tamanho e o estado dele.
O movimento (pulo e gravidade) fica em mecanica/movimento.py.
"""
import os
import pygame
from config import CHAO, AZUL, PASTA_IMAGENS


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
    imagem = pygame.image.load(os.path.join(PASTA_IMAGENS, 'personagem.png')).convert_alpha()
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
        janela.blit(imagens['abaixado'], (dino['x'], dino['y'] - pulinho))
    else:
        janela.blit(imagens['em_pe'], (dino['x'], dino['y'] - pulinho))

    # Se tem escudo, desenha um círculo azul em volta
    if dino['escudo']:
        centro = (dino['x'] + dino['largura'] // 2, dino['y'] + dino['altura'] // 2)
        pygame.draw.circle(janela, AZUL, centro, 36, 2)


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
        return {'tipo': tipo, 'x': LARGURA, 'y': CHAO - 48, 'largura': 20, 'altura': 48}
    elif tipo == 'cacto_grande':
        return {'tipo': tipo, 'x': LARGURA, 'y': CHAO - 58, 'largura': 34, 'altura': 58}
    else:
        # O ptero voa na altura da cabeça: em pé bate, abaixado passa por baixo
        return {'tipo': tipo, 'x': LARGURA, 'y': CHAO - 60, 'largura': 46, 'altura': 30}


def desenhar_obstaculo(janela, obs, frames):
    """Desenha um cacto (verde) ou um pterodáctilo (com asas batendo)."""
    x = obs['x']
    y = obs['y']
    if obs['tipo'] == 'ptero':
        pygame.draw.rect(janela, CINZA, (x + 6, y + 12, 34, 6))                                    # corpo
        pygame.draw.polygon(janela, CINZA, [(x + 40, y + 12), (x + 46, y + 15), (x + 40, y + 18)])  # bico
        if (frames // 10) % 2 == 0:   # asas para cima
            pygame.draw.polygon(janela, CINZA, [(x + 14, y + 13), (x + 24, y), (x + 28, y + 13)])
        else:                         # asas para baixo
            pygame.draw.polygon(janela, CINZA, [(x + 14, y + 17), (x + 24, y + 29), (x + 28, y + 17)])
    else:
        meio = x + obs['largura'] // 2
        pygame.draw.rect(janela, VERDE, (meio - 5, y, 10, obs['altura']))         # tronco
        pygame.draw.rect(janela, VERDE, (x, y + 14, 6, 14))                       # braço esquerdo
        pygame.draw.rect(janela, VERDE, (x, y + 24, obs['largura'] // 2, 5))
        pygame.draw.rect(janela, VERDE, (x + obs['largura'] - 6, y + 8, 6, 14))   # braço direito
        pygame.draw.rect(janela, VERDE, (meio, y + 18, obs['largura'] // 2, 5))


def criar_escudo():
    """Cria o power-up de escudo na direita da tela, um pouco acima do chão."""
    return {'x': LARGURA, 'y': CHAO - 36, 'largura': 26, 'altura': 26}


def desenhar_escudo(janela, escudo, fonte):
    """Desenha o escudo: um círculo azul com a letra S."""
    centro = (escudo['x'] + 13, escudo['y'] + 13)
    pygame.draw.circle(janela, AZUL, centro, 13)
    letra = fonte.render('S', True, (255, 255, 255))
    janela.blit(letra, letra.get_rect(center=centro))