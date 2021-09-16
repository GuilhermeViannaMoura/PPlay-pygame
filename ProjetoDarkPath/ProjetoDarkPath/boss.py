from imports import *
from random import uniform
from random import randint

relogio = 0
relogio2 = 0
velocidades = []

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
    vel1 = 500 * janela.delta_time()
    if relogio >= delay + uniform(0,1):
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

def rebate_ataque(player,rebate,atk):
    global velocidades
    for i in range(len(atk)):
        if atk[i].x <= player.x + player.width and rebate:
            velocidades[i] *= -1.5
