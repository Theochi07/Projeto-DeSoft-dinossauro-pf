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