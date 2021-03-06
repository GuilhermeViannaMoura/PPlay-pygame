from imports import *
from random import uniform
from random import randint

relogio = 0
relogio2 = 0
relogio3 = 0
velocidades = []
#acertou = False


def inicia_boss(pontos):
    if pontos == 10 or pontos == 150 or pontos == 250: # 40?
        return True
    else:
        return False

def desenha_bossf(janela,boss_final):
    boss_final.draw()
    boss_final.update()
    return

def ataques_boss(boss_atck1,boss_atck2,protecao,dif,janela,boss):
    global relogio
    global relogio2
    global velocidades
    if dif == "easy":
        delay = 2
    elif dif == "medium":
        delay = 1.5
    elif dif == "hard":
        delay = 1

    ### CRIA ATAQUES ###
    relogio += janela.delta_time()
    #vel1 = 500 * janela.delta_time()
    vel1 = 5 # essa velocidade com o delta_time estava gerando muitos bugs 
    if relogio >= delay:
        atck1 = Sprite("imagens/bosses/atck1.png")
        atck1.x = boss.x - atck1.width
        atck1.y = boss.y + randint(100,200)
        boss_atck1.append(atck1)
        velocidades.append(vel1)
        relogio = 0

    x = uniform(50,janela.width-200)
    relogio2 += janela.delta_time()
    if relogio2 >= delay - uniform(0.5,1):
        atck2 = Sprite("imagens/bosses/atck2-1.png")
        atck2.x = x
        atck2.y = -atck2.height
        boss_atck2.append(atck2)
        relogio2 = 0

    ### DESENHA ATAQUES ###
    protecao.draw()
    protecao.update()

    vel2 = 500 * janela.delta_time()

    for i in range(len(boss_atck2)):
        boss_atck2[i].draw()
        boss_atck2[i].move_y(vel2)
    for i in range(len(boss_atck1)):
        boss_atck1[i].draw()
        boss_atck1[i].move_x(-velocidades[i])

    return boss_atck1,boss_atck2

def rebate_ataque(player,rebate,atk,janela,vidas):
    global velocidades
    global relogio3
    relogio3 += janela.delta_time()
    for i in range(len(atk)):
        if atk[i].x <= player.x + player.width/2 + 30:
            vidas -= 1
            atk.pop(i)
            velocidades.pop(i)
        elif atk[i].x <= player.x + player.width and rebate and relogio3 >= 1:
            velocidades[i] *= -1.5
            relogio3 = 0

    return vidas

def colisao_rebatida_boss(atk,boss,vida_boss,janela,pontos):
    global velocidades
    for i in range(len(atk)):
        if atk[i].x >= boss.x + 50:
            atk.pop(i)
            velocidades.pop(i)
            vida_boss -= 1
            pontos += 2
            break

    janela.draw_text("VIDAS BOSS: %d"%vida_boss,janela.width-200,10,20,color=(150,150,150),font_name="Arial",bold=True)
    return vida_boss,pontos
