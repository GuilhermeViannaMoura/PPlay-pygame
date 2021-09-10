from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import randint
from random import uniform
from player import fim_vidas

pontos = 0
tempo = 5
fase = 1 # interfere na velocidade de movimentacao dos inimigos e no delay dos tiros inimigos
num_inimigos_vivos = 40 # max
n_linhas = 3 #5 max
n_colunas = 4 #8 max
linhaInimigoForte = randint(0,n_linhas-1)
colunaInimigoForte = randint(0,n_colunas-1)
forte = True
naveForte = 1


def cria_inimigos():
    global num_inimigos_vivos
    global naveForte
    global forte
    num_inimigos_vivos = 40
    inimigos = []
    forte = True

    for i in range(n_linhas):
        inimigos.append([])

    for i in range(n_linhas):
        for j in range(n_colunas):
            if i == linhaInimigoForte and j == colunaInimigoForte: # gera inimigo forte
                naveInimiga = Sprite("imagens/inimigo3.png")
                inimigos[i].append(naveInimiga)
                naveInimiga.x = (naveInimiga.width * 1.1) * j + 5 # posição inicial das naves inimigas
                naveInimiga.y = (naveInimiga.height * 1.1) * i + 5
                naveForte = naveInimiga
            else:
                naveInimiga = Sprite("imagens/inimigo2.png")
                inimigos[i].append(naveInimiga)
                naveInimiga.x = (naveInimiga.width * 1.1) * j + 5 # posição inicial das naves inimigas
                naveInimiga.y = (naveInimiga.height * 1.1) * i + 5

    return inimigos

def desenha_inimigos(inimigos,vel_inimigo,janela):
    global num_inimigos_vivos
    for i in range(len(inimigos)):
        for j in range(len(inimigos[i])):
            inimigos[i][j].draw()
            inimigos[i][j].move_x(vel_inimigo*janela.delta_time()*fase/(num_inimigos_vivos/40)) # velocidade dos inimigos
            if num_inimigos_vivos < 10:
                num_inimigos_vivos = 10

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

def colisao_tiro_inimigo(tiros,inimigos,janela):
    sair = False
    try:
        x_esq = inimigos[0][0].x
        x_dir = inimigos[0][-1].x + inimigos[0][-1].width
        y_baixo = inimigos[-1][-1].y + inimigos[-1][-1].height
        y_cima = inimigos[0][0].y
        global pontos
        global num_inimigos_vivos
        global forte
        janela.draw_text("PONTOS: %d" %pontos,janela.width-150,10,size=20,color=(0,0,0))
        for i in range(len(tiros)):
            if (tiros[i].y < y_baixo and tiros[i].y > y_cima and
            tiros[i].x < x_dir and tiros[i].x > x_esq): #optimização dos tiros
                for j in range(len(inimigos)-1,-1,-1): #checa colisao primeiro nos inimigos de baixo
                    for k in range(len(inimigos[j])):
                        if tiros[i].collided(inimigos[j][k]):
                            if inimigos[j][k] == naveForte and forte == True:
                                naveInimiga = Sprite("imagens/inimigo2.png")
                                naveInimiga.x = inimigos[j][k].x
                                naveInimiga.y = inimigos[j][k].y
                                inimigos[j][k] = naveInimiga
                                tiros.pop(i)
                                sair = True
                                forte = False
                                pontos += 10
                                break
                            else:
                                inimigos[j].pop(k)
                                if len(inimigos[-1]) == 0:
                                    inimigos.pop(-1) #retira lista vazia quando todos os monstros da linha são destruídos
                                tiros.pop(i)
                                sair = True
                                pontos += 10
                                num_inimigos_vivos -= 1
                                break
                    if sair:
                        break
            if sair:
                break
    except IndexError:
        pass
    return pontos

def atira_inimigo(tiros,inimigos,janela,dificuldade): # Cria e trata cada tiro separadamente
    if dificuldade == "easy":
        delayTiro = 3.0 - fase + num_inimigos_vivos/10
    elif dificuldade == "medium":
        delayTiro = 2.0 - fase + num_inimigos_vivos/10
    elif dificuldade == "hard":
        delayTiro = 1.0 - fase + num_inimigos_vivos/10

    global tempo
    tempo += janela.delta_time()
    if tempo >= delayTiro + uniform(0,0.5):
        tiro = Sprite("imagens/laserGreen.png")
        xi = randint(0,len(inimigos)-1)
        yi = randint(0,len(inimigos[0])-1)
        try:
            tiro.x = inimigos[xi][yi].x + 45
            tiro.y = inimigos[xi][yi].y + tiro.height
            tiros.append(tiro)
            tempo = 0
        except IndexError: # caso a nave sorteada tenha sido destruida
            pass
    
    i = 0
    while i < len(tiros):
        tiros[i].y += 700 * janela.delta_time()
        tiros[i].draw()
        if tiros[i].y + tiros[i].height > janela.height:
            tiros.pop(i)
        else:
            i += 1
    
    return tiros

def fim(inimigos,nave,janela):
    global pontos
    global n_linhas
    global n_colunas
    if inimigos[-1][-1].y + inimigos[-1][-1].height >= nave.y or fim_vidas():
        nave.x = janela.width/2 - nave.width/2
        nave.y = janela.height - nave.height - 10
        nome = input("Digite seu nome para o ranking: ")
        linha = nome + " " + str(pontos) + "\n"
        arq = open("rank.txt","a")
        arq.writelines(linha)
        arq.close()
        pontos = 0
        n_linhas = 3
        n_colunas = 4
        return True
    else:
        return False

def nova_fase(inimigos):
    global fase
    global n_linhas
    global n_colunas
    if inimigos == []:
        if n_linhas < 5:
            n_linhas += 1
        if n_colunas < 8:
            n_colunas += 1
        inimigos = cria_inimigos()
        fase += 0.3
    
    return inimigos