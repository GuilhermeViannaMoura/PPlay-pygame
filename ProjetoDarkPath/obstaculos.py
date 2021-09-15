from imports import *
from random import randint

rel = 0

def cria_obstaculos(janela,obstaculos,obstaculos2,lbarras):
    global rel
    r = randint(1,3)
    rel += janela.delta_time()
    #obstaculos2 eh uma lista com sprites com uma hitbox que funciona melhor para o tamanho que eh desenhado da lista obstaculos
    if r == 1 and rel >= 2:
        spikes = Sprite("imagens/obstaculos/spikes.png")
        spikes2 = Sprite("imagens/obstaculos/spikes2.png")
        spikes.x = janela.width -50
        spikes.y = janela.height - spikes.height
        spikes2.x = spikes.x + spikes2.width/2 - 30
        spikes2.y = spikes.y + spikes.height/2
        obstaculos.append(spikes)
        obstaculos2.append(spikes2)
        rel = 0
    elif r == 2 and rel >= 2:
        blade = Sprite("imagens/obstaculos/blade.png")
        blade2 = Sprite("imagens/obstaculos/blade2.png")
        blade.x = janela.width -50
        blade.y = janela.height - blade.height/2
        blade2.x = blade.x + blade2.width/2 - 30
        blade2.y = blade.y + 50
        obstaculos.append(blade)
        obstaculos2.append(blade2)
        rel = 0
    elif r == 3 and rel >= 2:
        barra = Sprite("imagens/obstaculos/barra.png")
        barra.x = janela.width -50
        barra.y = -160
        obstaculos.append(barra)
        lbarras.append(barra) # lista para tratar a colisao das barras de forma diferentes aos outros obstaculos
        rel = 0
    
    return obstaculos,obstaculos2,lbarras

def desenha_obstaculos(obstaculos, janela,obstaculos2,lbarras):
    vel_obstaculo = -400 * janela.delta_time()
    for i in range(len(obstaculos)): # MOVE E DESENHA OS OBSTACULOS
        obstaculos[i].draw()
        obstaculos[i].move_x(vel_obstaculo)
    for i in range(len(obstaculos2)): # LISTA DAS HITBOXES ACOMPANHA O OBSTACULO REAL
        obstaculos2[i].move_x(vel_obstaculo)
    # for i in range(len(lbarras)):
    #     lbarras[i].move_x(vel_obstaculo) #DESCOMENTAR ESSE TRECHO FARÁ AS BARRAS SE MOVEREM NO DOBRO DA VELOCIDADE