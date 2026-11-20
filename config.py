"""Constantes do jogo: tamanhos, física, dificuldade, cores e estados.

Para deixar o jogo mais fácil ou mais difícil, basta mudar os números daqui.
"""
import os

# ----- Janela -----
LARGURA = 900
ALTURA = 300
FPS = 60
CHAO = 250                 # altura (y) da linha do chão

# ----- Física do pulo -----
GRAVIDADE = 0.9            # quanto o dino acelera para baixo a cada frame
FORCA_PULO = -14           # velocidade do pulo (negativo = para cima)

# ----- Dificuldade -----
VELOCIDADE_INICIAL = 10    # velocidade dos obstáculos na fase 1
AUMENTO_POR_FASE = 1.6     # quanto a velocidade aumenta a cada fase
PONTOS_POR_FASE = 200      # a cada 200 pontos muda de fase
FASE_MAXIMA = 10
TEMPO_ESCUDO = 1800        # um escudo aparece a cada 1800 frames (30 segundos)
PONTOS_PARA_VENCER = 2500  # chegou nesses pontos, venceu o jogo

# ----- Cores (vermelho, verde, azul) -----
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (83, 83, 83)
CINZA_CLARO = (170, 170, 170)
VERDE = (40, 140, 60)
AZUL = (50, 120, 230)
AMARELO = (250, 200, 40)
CEU = (225, 240, 255)

# ----- Estados do jogo (qual tela está aparecendo) -----
SAIR = 0
MENU = 1
INSTRUCOES = 2
JOGANDO = 3
GAME_OVER = 4
VITORIA = 5

# ----- Pastas onde ficam os sons e a imagem do personagem -----
PASTA_SONS = os.path.join(os.path.dirname(__file__), 'sons')
PASTA_IMAGENS = os.path.join(os.path.dirname(__file__), 'personagem')
