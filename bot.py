import random


def bot_tic_tac(zapolnenie):
    c = False
    while c == False:
        num = random.randint(0,8)
        if zapolnenie[num] == '-':
            zapolnenie[num] = 'O'
            c = True
    return zapolnenie