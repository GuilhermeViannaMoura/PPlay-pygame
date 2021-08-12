from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from menu import *

tempo = 5

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

def atira(teclado,tiros,nave,janela): # Cria e trata cada tiro separadamente
    global dificuldade
    if dificuldade == "easy":
        delayTiro = 0.2
    elif dificuldade == "medium":
        delayTiro = 0.5
    elif dificuldade == "hard":
        delayTiro = 1.5

    global tempo
    tempo += janela.delta_time()
    if teclado.key_pressed("SPACE") and tempo >= delayTiro:
        tiro = Sprite("LabJogos/ProjetoSpaceInvaders/imagens/tiro.png")
        tiro.x = nave.x + 45
        tiro.y = nave.y - tiro.height
        tiros.append(tiro)
        tempo = 0
    
    i = 0
    while i < len(tiros):
        tiros[i].y -= 1000 * janela.delta_time()
        tiros[i].draw()
        if tiros[i].y + tiros[i].height < 0:
            tiros.pop(i)
        else:
            i += 1