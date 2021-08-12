from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

dificuldade = "medium"

def menu(janela):
    #Inicializacao
    mouse = Window.get_mouse()
    fundo = GameImage("LabJogos/ProjetoSpaceInvaders/imagens/starBackground.jpg")
    play_button = Sprite("LabJogos/ProjetoSpaceInvaders/imagens/buttons/play.png")
    level_button = Sprite("LabJogos/ProjetoSpaceInvaders/imagens/buttons/level select.png")
    quit_button = Sprite("LabJogos/ProjetoSpaceInvaders/imagens/buttons/quit.png")
    easy_button = Sprite("LabJogos/ProjetoSpaceInvaders/imagens/buttons/easy_button.png")
    medium_button = Sprite("LabJogos/ProjetoSpaceInvaders/imagens/buttons/medium_button.png")
    hard_button = Sprite("LabJogos/ProjetoSpaceInvaders/imagens/buttons/hard_button.png")
    rank_button = Sprite("LabJogos/ProjetoSpaceInvaders/imagens/buttons/rank.png")
    title = Sprite("LabJogos/ProjetoSpaceInvaders/imagens/title.png")


    #Posicoes dos botoes
    play_button.x = janela.width/2 - 150
    play_button.y = janela.height -315

    level_button.x = janela.width/2 - 150
    level_button.y = janela.height -225

    quit_button.x = janela.width/2 - 150
    quit_button.y = janela.height - 135

    easy_button.x = janela.width/2 - 150
    easy_button.y = janela.height/2 - 120

    medium_button.x = janela.width/2 - 150
    medium_button.y = janela.height/2 - 30

    hard_button.x = janela.width/2 - 150
    hard_button.y = janela.height/2 + 60

    rank_button.x = 1
    rank_button.y = janela.height - 100

    title.x = janela.width/2 - 370
    title.y = 100

    c_menu = "home"

    #Menu Loop
    while (True):

        #Menu State
        if c_menu == "home": # HOME DO MENU
            fundo.draw()
            play_button.draw()
            level_button.draw()
            quit_button.draw()
            rank_button.draw()
            title.draw()
            if mouse.is_over_object(play_button):
                play_button.x = janela.width/2 - 130 #destaca botao quando mouse esta em cima
                if mouse.is_button_pressed(1):
                    c_menu = "play"
            elif mouse.is_over_object(level_button):
                level_button.x = janela.width/2 - 130 #destaca botao quando mouse esta em cima
                if mouse.is_button_pressed(1):
                    c_menu = "level"
            elif mouse.is_over_object(quit_button):
                quit_button.x = janela.width/2 -130 #destaca botao quando mouse esta em cima
                if mouse.is_button_pressed(1):
                    c_menu = "quit"
            else:
                #encerra o destaque dos botoes quando o mouse nao esta mais em cima deles
                play_button.x = janela.width/2 - 150 
                level_button.x = janela.width/2 - 150
                quit_button.x = janela.width/2 - 150

        elif c_menu == "play":
            return "jogo" #esse retorno interfere na variavel de controle de jogo da main

        elif c_menu == "level": # TELA DE ESCOLHA DA DIFICULDADE
            fundo.draw()
            easy_button.draw()
            medium_button.draw()
            hard_button.draw()
            global dificuldade
            if mouse.is_over_object(easy_button):
                easy_button.x = janela.width/2 - 130  #destaca botao quando mouse esta em cima
                if mouse.is_button_pressed(1):
                    dificuldade = "easy"
                    c_menu = "home"
            elif mouse.is_over_object(medium_button):
                medium_button.x = janela.width/2 - 130 #destaca botao quando mouse esta em cima
                if mouse.is_button_pressed(1):
                    dificuldade = "medium"
                    c_menu = "home"
            elif mouse.is_over_object(hard_button):
                hard_button.x = janela.width/2 - 130 #destaca botao quando mouse esta em cima
                if mouse.is_button_pressed(1):
                    dificuldade = "hard"
                    c_menu = "home"
            else:
                #encerra o destaque dos botoes quando o mouse nao esta mais em cima deles
                easy_button.x = janela.width/2 - 150
                medium_button.x = janela.width/2 - 150
                hard_button.x = janela.width/2 - 150

        elif c_menu == "quit":
            quit()
        janela.update()