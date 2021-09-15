from imports import *
from player import *
from menu import *
from obstaculos import *

janela = Window(1600,900)
teclado = Window.get_keyboard()
janela.set_title("Dark Path")

player_running = Sprite("imagens/player/run.png",9)
player_running.set_total_duration(800)
player_running.x = 100
player_running.y = janela.height - player_running.height
py = janela.height - player_running.height

player_jump = Sprite("imagens/player/jumpp.png",7)
player_jump.set_total_duration(600)
player_jump.x = player_running.x
player_jump.y = player_running.y

player_sliding = Sprite("imagens/player/slide.png")
player_sliding.x = player_running.x
player_sliding.y = player_running.y + 50

player_attack = Sprite("imagens/player/attack3.png",6)
player_attack.set_total_duration(300)
player_attack.x = player_running.x
player_attack.y = player_running.y - 50

fundo = Sprite("imagens/fundo2.png")
fundo2 = Sprite("imagens/fundo2.png")
fundo.x = 0
fundo.y = 0
fundo2.x = 0
fundo2.y = 0
fx = 0

obstaculos = []
obstaculos2 = []
lbarras = []

music_menu = Sound("musicas/Menu Music.wav")
music_fase = Sound("musicas/In-game-Running-music.wav")
music_fase.set_volume(5)

controle = "menu"

while True:
    if controle == "menu":
        music_fase.stop()
        music_menu.play()
        controle, dif = menu(janela)
        obstaculos = []
    elif controle == "jogo":
        music_menu.stop()
        music_fase.play()
        ### DESENHA FUNDO ###
        rel_x = fx % fundo.width
        fundo.x = rel_x - fundo.width
        if rel_x < janela.width:
            fundo2.x = rel_x
            fundo2.draw()
        fx -= 500 * janela.delta_time()
        fundo.draw()

        ### DESENHA PLAYER ###
        player(player_sliding,player_jump,player_running,player_attack,janela,teclado,py)

        ### DESENHA OBSTACULOS ###
        obstaculos,obstaculos2,lbarras = cria_obstaculos(janela,obstaculos,obstaculos2,lbarras)
        desenha_obstaculos(obstaculos,janela,obstaculos2,lbarras)
        controle,obstaculos2,lbarras = colisao_player_obstaculo(player_running,obstaculos2,lbarras,teclado)
        #controle,lbarras = colisao_player_barra(player_running,lbarras,teclado)


        janela.update()
