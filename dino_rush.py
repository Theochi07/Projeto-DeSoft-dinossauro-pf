    """Dino Rush - arquivo principal. Execute este arquivo para jogar

    Abre a janela, carrega fontes e sons e controla qual tela aparece
    (máquina de estados). O recorde vale enquanto o jogo estiver aberto.
    """
    import pygame
    from config import LARGURA, ALTURA, SAIR, MENU, INSTRUCOES, JOGANDO, GAME_OVER, VITORIA
    from sons.sons import carregar_sons
    from personagem.dino import carregar_imagens_dino
    from tela.menu import tela_menu
    from tela.instrucoes import tela_instrucoes
    from tela.jogo import tela_jogo
    from tela.game_over import tela_game_over
    from tela.vitoria import tela_vitoria

    # ----- Inicialização -----
    pygame.init()
    pygame.mixer.init()
    janela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Dino Rush')

    fontes = {
        'grande': pygame.font.SysFont(None, 64),
        'normal': pygame.font.SysFont(None, 30),
    }
    sons = carregar_sons()
    imagens = carregar_imagens_dino()

    # ----- Máquina de estados: cada tela devolve qual é a próxima -----
    estado = MENU
    recorde = 0
    pontos = 0

    while estado != SAIR:
        if estado == MENU:
            estado = tela_menu(janela, fontes, imagens, recorde)
        elif estado == INSTRUCOES:
            estado = tela_instrucoes(janela, fontes)
        elif estado == JOGANDO:
            estado, pontos = tela_jogo(janela, fontes, sons, imagens)
            if pontos > recorde:
                recorde = pontos
        elif estado == GAME_OVER:
            estado = tela_game_over(janela, fontes, sons, pontos, recorde)
        elif estado == VITORIA:
            estado = tela_vitoria(janela, fontes, sons, imagens, pontos)

    # ----- Finalização -----
    pygame.quit()
