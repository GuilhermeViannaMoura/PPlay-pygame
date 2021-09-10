from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

tempo = 5
nVidas = 3
pisca = False
tempo2 = 0
nP = 0
caso = 2


def pMove(nave,teclado,janela): # Movimentação da nave
    velocidade = 300 * janela.delta_time() # Velocidade da nave
    if teclado.key_pressed("LEFT"):
        nave.move_x(-velocidade)

    if teclado.key_pressed("RIGHT"):
        nave.move_x(velocidade)
    
    if nave.x + nave.width > janela.width:
        nave.x = janela.width - nave.width
    elif nave.x < 0:
        nave.x = 0

def atira(teclado,tiros,nave,janela,dificuldade): # Cria e trata cada tiro separadamente
    # global dificuldade
    if dificuldade == "easy":
        delayTiro = 0.3
    elif dificuldade == "medium":
        delayTiro = 0.5
    elif dificuldade == "hard":
        delayTiro = 0.7

    global tempo
    tempo += janela.delta_time()
    if teclado.key_pressed("SPACE") and tempo >= delayTiro:
        tiro = Sprite("imagens/tiro.png")
        tiro.x = nave.x + 45
        tiro.y = nave.y - tiro.height
        tiros.append(tiro)
        tempo = 0
    
    i = 0
    while i < len(tiros):
        tiros[i].y -= 1500 * janela.delta_time() # velocidade tiro
        tiros[i].draw()
        if tiros[i].y + tiros[i].height < 0:
            tiros.pop(i)
        else:
            i += 1
    
    return tiros

def colisao_tiro_nave(tiros,nave,janela):
    global nVidas
    global pisca
    global tempo2
    global nP
    global caso

    for i in range(len(tiros)):
        if tiros[i].collided(nave) and not pisca:
            tiros.pop(i)
            nVidas -= 1
            nave.x = janela.width/2 - nave.width/2
            pisca = True
            break
    
    # deixa o player imortal enquanto pisca na tela após receber um tiro
    if nP == 4:
        pisca = False
        nP = 0
    tempo2 += janela.delta_time()
    if pisca and tempo2 >= 0.2:
        if caso == 1:
            nave.unhide()
            nP += 1
            caso = 2
        elif caso == 2:
            nave.hide()
            caso = 1
        tempo2 = 0
    
    return nVidas

def fim_vidas():
    global nVidas
    if nVidas == 0:
        nVidas = 3
        return True
    else:
        return False