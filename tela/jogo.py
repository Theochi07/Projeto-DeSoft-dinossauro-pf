"""Tela do jogo: o loop principal da partida.

A cada frame: lê o teclado, atualiza pontos e fase, cria obstáculos,
move tudo, testa colisões e desenha a tela.
"""
import pygame
from config import (LARGURA, ALTURA, FPS, PRETO, AZUL, VELOCIDADE_INICIAL, TEMPO_ESCUDO,
                    PONTOS_PARA_VENCER, SAIR, GAME_OVER, VITORIA)
from personagem.dino import criar_dino, desenhar_dino
from obstaculos.obstaculos import criar_obstaculo, desenhar_obstaculo, criar_escudo, desenhar_escudo
from mecanica.movimento import (pular, atualizar_dino, mover_obstaculos)

from mecanica.colisao import bateu

from mecanica.fases import (calcular_fase, calcular_velocidade, sortear_intervalo)
from cenario.cenario import escrever, desenhar_cenario, desenhar_chao
from sons.sons import tocar, tocar_musica


def tela_jogo(janela, fontes, sons, imagens):
    """Loop principal da partida. Retorna (próximo estado, pontos)."""
    relogio = pygame.time.Clock()
    tocar_musica()

    dino = criar_dino()
    obstaculos = []            # lista de dicionários
    escudo = None              # None = não tem escudo na tela
    frames = 0
    pontos = 0
    fase = 1
    velocidade = VELOCIDADE_INICIAL
    proximo_obstaculo = 60     # frames até criar o próximo obstáculo
    proximo_escudo = TEMPO_ESCUDO
    pausado = False
    mensagem = ''
    tempo_mensagem = 0         # por quantos frames a mensagem fica na tela

    while True:
        relogio.tick(FPS)

        # ---------- 1. Eventos (teclado e fechar janela) ----------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return SAIR, pontos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausado = not pausado
                if event.key == pygame.K_UP and not pausado:
                    if pular(dino):
                        tocar(sons, 'pulo')

        if pausado:
            escrever(janela, fontes['grande'], 'PAUSADO (P)', PRETO, LARGURA / 2, ALTURA / 2)
            pygame.display.update()
            continue   # pula o resto e volta para o começo do while

        teclas = pygame.key.get_pressed()
        atualizar_dino(dino, teclas[pygame.K_DOWN])

        # ---------- 2. Pontos, fase e vitória ----------
        frames = frames + 1
        pontos = frames // 6              # 10 pontos por segundo
        nova_fase = calcular_fase(pontos)
        if nova_fase > fase:
            fase = nova_fase
            velocidade = calcular_velocidade(fase)
            mensagem = 'FASE ' + str(fase) + '!'
            tempo_mensagem = 2 * FPS
            tocar(sons, 'fase')

        if pontos >= PONTOS_PARA_VENCER:
            return VITORIA, pontos

        # ---------- 3. Cria obstáculos e escudo ----------
        proximo_obstaculo = proximo_obstaculo - 1
        if proximo_obstaculo <= 0:
            obstaculos.append(criar_obstaculo(fase))
            proximo_obstaculo = sortear_intervalo(fase)

        proximo_escudo = proximo_escudo - 1
        if proximo_escudo <= 0:
            if not dino['escudo']:
                escudo = criar_escudo()
            proximo_escudo = TEMPO_ESCUDO

        # ---------- 4. Move tudo ----------
        obstaculos = mover_obstaculos(obstaculos, velocidade)
        if escudo is not None:
            escudo['x'] = escudo['x'] - velocidade
            if escudo['x'] + escudo['largura'] < 0:
                escudo = None

        # ---------- 5. Colisões ----------
        if escudo is not None and bateu(dino, escudo):
            dino['escudo'] = True
            escudo = None
            mensagem = 'ESCUDO ATIVADO!'
            tempo_mensagem = 2 * FPS

        for obs in obstaculos:
            if bateu(dino, obs):
                if dino['escudo']:
                    dino['escudo'] = False
                    obstaculos.remove(obs)   # o escudo destrói o obstáculo
                    tocar(sons, 'batida')
                    mensagem = 'O ESCUDO QUEBROU!'
                    tempo_mensagem = 2 * FPS
                    break
                else:
                    return GAME_OVER, pontos

        # ---------- 6. Desenha ----------
        desenhar_cenario(janela, frames * velocidade)
        desenhar_chao(janela, frames * velocidade)
        desenhar_dino(janela, dino, frames, imagens)
        for obs in obstaculos:
            desenhar_obstaculo(janela, obs, frames)
        if escudo is not None:
            desenhar_escudo(janela, escudo, fontes['normal'])

        escrever(janela, fontes['normal'], 'Pontos: ' + str(pontos) + ' / ' + str(PONTOS_PARA_VENCER) +
                 '   Fase: ' + str(fase), PRETO, LARGURA / 2, 20)
        if tempo_mensagem > 0:
            escrever(janela, fontes['normal'], mensagem, AZUL, LARGURA / 2, 55)
            tempo_mensagem = tempo_mensagem - 1

        pygame.display.update()
