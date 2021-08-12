from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

def cria_inimigos():
    n_linhas = 5
    n_colunas = 8
    inimigos = []

    for i in range(n_linhas):
        inimigos.append([])

    for i in range(n_linhas):
        for j in range(n_colunas):
            naveInimiga = Sprite("LabJogos/ProjetoSpaceInvaders/imagens/inimigo2.png")
            inimigos[i].append(naveInimiga)
            naveInimiga.x = (naveInimiga.width * 1.5) * j + 5 # posição inicial das naves inimigas
            naveInimiga.y = (naveInimiga.height * 1.5) * i + 5

    return inimigos

def desenha_inimigos(inimigos,vel_inimigo,janela):
    for i in range(len(inimigos)):
        for j in range(len(inimigos[i])):
            inimigos[i][j].draw()
            inimigos[i][j].move_x(vel_inimigo*janela.delta_time())

def colisao_inimigo_parede(inimigos,janela,vel_inimigo):
    caso = 0
    for i in range(len(inimigos)):
        for j in range(len(inimigos[i])):
            if (inimigos[i][j].x + inimigos[i][j].width) >= janela.width or inimigos[i][j].x <= 0:
                vel_inimigo = -vel_inimigo # muda a direção dos inimigos
                caso = 2 if inimigos[i][j].x <= 0 else 1 # registra qual caso ocorreu
                corrige_bug_patinacao(inimigos,caso)
                for i in range(len(inimigos)):
                    for j in range(len(inimigos[i])):
                        inimigos[i][j].y += 20 # avança os inimigos
                return vel_inimigo # retorna velocidade invertida
    return vel_inimigo # retorna velocidade mantendo direção

def corrige_bug_patinacao(inimigos,caso):
    for i in range(len(inimigos)):
        for j in range(len(inimigos[i])):
            if caso == 1:
                inimigos[i][j].x -= 3
            elif caso == 2:
                inimigos[i][j].x += 3