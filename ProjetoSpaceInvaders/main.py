from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from menu import *
from player import *
from monstros import *

controle = "menu"

#Inicialização
janela = Window(900,907)
teclado = Window.get_keyboard()
janela.set_title("SpaceInvaders")

nave = Sprite("imagens/player.png")
nave.x = janela.width/2 - nave.width/2
nave.y = janela.height - nave.height - 10

game_background = Sprite("imagens/starBackground.jpg")


tiros = []
tiros_inimigos = []
inimigos = cria_inimigos()
vel_inimigo = 100
relogio = 0
nFrames = 0
fps = 0
pontos = 0
# nVidas = 3
reinicia = False

#GAME LOOP
while True:
    if controle == "menu":
        controle, dif = menu(janela)
    elif controle == "jogo": #Inicia o Jogo
        janela.set_background_color((0,0,0))
        game_background.draw()
        nave.draw()
        vel_inimigo = colisao_inimigo_parede(inimigos,janela,vel_inimigo)
        desenha_inimigos(inimigos,vel_inimigo,janela)
        pMove(nave,teclado,janela)
        projeteis = atira(teclado,tiros,nave,janela,dif)
        pontuacao = colisao_tiro_inimigo(projeteis,inimigos,janela)
        atira_inimigo(tiros_inimigos,inimigos,janela,dif)
        numVidas = colisao_tiro_nave(tiros_inimigos,nave,janela)
        #FPS
        relogio += janela.delta_time()
        nFrames += 1
        if relogio>=1:
            fps = nFrames
            nFrames = 0
            relogio = 0
        janela.draw_text("FPS: %d" %fps,10,10,size=20,color=(0,0,0),font_name="Arial",bold=True)
        janela.draw_text("VIDAS: %d" %numVidas,10,30,size=20,color=(0,0,0),font_name="Arial",bold=True)

        # volta para o menu
        if teclado.key_pressed("ESC"):
            controle = "menu"

        # nova fase
        inimigos = nova_fase(inimigos)

        # verifica fim de jogo e reinicia
        try:
            reinicia = fim(inimigos,nave,janela)
        except IndexError:
            pass
        if reinicia:
            inimigos = cria_inimigos()
            reinicia = False
            controle = "menu"

        janela.update()