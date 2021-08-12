from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import choice
from random import randint

#Inicialização
janela = Window(1024,768)
janela.set_title("Pong")
teclado = Window.get_keyboard()

fundo = GameImage("LabJogos/ProjetoPong/imagens/fundo.jpg")
bola = Sprite("LabJogos/ProjetoPong/imagens/bola.png", 1)
padD = Sprite("LabJogos/ProjetoPong/imagens/paddle_green.png",1)
padE = Sprite("LabJogos/ProjetoPong/imagens/paddle_blue.png",1)
boost_esq = Sprite("LabJogos/ProjetoPong/imagens/boost_arrow_esquerda.png",1)
boost = Sprite("LabJogos/ProjetoPong/imagens/boost_arrow.png",1)

bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2
velBola = 450
velx = velBola * choice((-1,1)) #choice serve para a bola sempre começar em direcoes aleatorias
vely = velBola * choice((-1,1))

padD.x = janela.width - 35 - padD.width/2
padD.y = janela.height/2 - padD.height/2
padE.x = 35 - padE.width/2
padE.y = janela.height/2 - padE.height/2
velPad = 400
velPadInimigo = 600

boost.x = randint(padE.x + 30, padD.x-boost.width-30)
boost.y = randint(0, janela.height - boost.height)
boost_esq.x = boost.x
boost_esq.y = boost.y

pontD = 0 #pontuacao
pontE = 0
pontMax = 5

fps = 0
nFrames = 0
relogio = 0
relogio2 = 0
velBoost = 1
controleJogo = True
esperaPonto = True

def reiniciar():
    padD.x = janela.width - 35 - padD.width/2
    padD.y = janela.height/2 - padD.height/2
    padE.x = 35 - padE.width/2
    padE.y = janela.height/2 - padE.height/2
    bola.x = janela.width/2 - bola.width/2
    bola.y = janela.height/2 - bola.height/2
    return True


#Game Loop
while(True):
    if controleJogo:
        #Entrada de dados
        if teclado.key_pressed("UP") and padD.y >= 0:
            padD.move_y(-velPad*janela.delta_time()) # correcao de tempo
        if teclado.key_pressed("DOWN") and (padD.y + padD.height) <= janela.height:
            padD.move_y(velPad*janela.delta_time())

        #Update dos Game Objects
        if esperaPonto == False:
            bola.move_x(velx*janela.delta_time()*velBoost)
            bola.move_y(vely*janela.delta_time()*velBoost)
        else:
            relogio += janela.delta_time()
            if relogio>=1:
                esperaPonto = False
                velBoost = 1
                relogio = 0

            #Comportamento pad oponente
        if padE.y < bola.y and (padE.y + padE.height) < (janela.height - 60):
            padE.move_y(velPadInimigo*janela.delta_time())
        if (padE.y + padE.height) > bola.y and padE.y > 60:
            padE.move_y(-velPadInimigo*janela.delta_time())

            #FPS
        dt = janela.delta_time()
        relogio2 += dt
        nFrames += 1
        if relogio2>=1:
            fps = nFrames
            nFrames = 0
            relogio2 = 0

        #Game Physics
        if bola.x + bola.width >= janela.width:
            pontE += 1
            bola.x = janela.width/2 - bola.width/2 # reseta bolinha
            bola.y = janela.height/2 - bola.height/2
            velx = velBola * choice((-1,1))
            vely = velBola * choice((-1,1))
            esperaPonto = True
            
        if bola.x <= 0:
            pontD += 1
            bola.x = janela.width/2 - bola.width/2 # reseta bolinha
            bola.y = janela.height/2 - bola.height/2
            velx = velBola * choice((-1,1))
            vely = velBola * choice((-1,1))
            esperaPonto = True

        if bola.y + bola.height > janela.height:
            bola.y = janela.height - bola.height # correção da patinação
            vely = -vely

        if bola.y < 0:
            bola.y = 0 # correção da patinação
            vely = -vely

        if padE.collided(bola) and (bola.x <= padE.x + padE.width):
            bola.x = padE.x + padE.width + 1 # correção da patinação
            velx = -velx
            velBoost = 1

        if padD.collided(bola) and (bola.x + bola.width >= padD.x):
            bola.x = padD.x - 1 - bola.width # correção da patinação
            velx = -velx
            velBoost = 1
        
        if boost.collided(bola):
            velBoost = 1.5
            boost.x = randint(padE.x + 30, padD.x-boost.width-30) # atualiza posicao do boost
            boost.y = randint(0, janela.height - boost.height)
            boost_esq.x = boost.x
            boost_esq.y = boost.y

        #Endgame
        if pontE == pontMax or pontD == pontMax:
            controleJogo = False

        #Desenho dos Game Objects
        janela.set_background_color((255,255,0))
        fundo.draw()
        bola.draw()
        padD.draw()
        padE.draw()
        if velx > 0:
            boost.draw()
        else:
            boost_esq.draw()
        janela.draw_text("%d" %pontE,janela.width/2-200,10,size=80,color=(0,0,0))
        janela.draw_text("%d" %pontD,janela.width/2+160,10,size=80,color=(0,0,0))
        janela.draw_text("FPS: %d" %fps,10,20,size=20,color=(0,0,0))
    
    else:
        if pontE == pontMax:
            xf = janela.width/2 -300
            yf = janela.height/2 -300 # posiciona o texto logo abaixo do placar
            janela.draw_text("Você Perdeu!" ,xf,yf,size=100,color=(0,0,0))
            xr = janela.width/2 -300
            yr = janela.height/2 -100
            janela.draw_text("Pressione 'espaço' para recomeçar" ,xr,yr,size=40,color=(0,0,0))
            if teclado.key_pressed("SPACE"):
                controleJogo = reiniciar()
                pontE, pontD = 0, 0
        elif pontD == pontMax:
            xf = janela.width/2 -300
            yf = janela.height/2 -300
            janela.draw_text("Você Ganhou!" ,xf,yf,size=100,color=(0.5,0.5,0))
            xr = janela.width/2 -300
            yr = janela.height/2 -100
            janela.draw_text("Pressione 'espaço' para recomeçar" ,xr,yr,size=40,color=(0,0,0))
            if teclado.key_pressed("SPACE"):
                controleJogo = reiniciar()
                pontE, pontD = 0, 0
    
    
    janela.update()