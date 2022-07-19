START = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
zapolnenie = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
#zapolnenie = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', '-']
WIN_KOMBO = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]




def has_free(move, prever):
    for i in range(0, 9):
        if move[i] == 'X':
            prever += 1
        if move[i] == 'O':
            prever += 1
    if prever == 9:
        return True
    else:
        return False

def check_plaers(num):
    if num is not None and num.isdigit() and int(num) in range(1, 3):
        print('Количество игроков:', num)
        return True

def check_mistake(num:str):
    if num is not None and num.isdigit() and int(num) in range(1,10):
        if zapolnenie[int(num) - 1] == '-':
            return True
    return False


def set_vell(num, posit='X'):
    zapolnenie[int(num)-1] = posit
    return zapolnenie


def check_win_x(move):
    for i in WIN_KOMBO:
        prevecs = 0
        for j in i:
            if move[j-1] == 'X':
                prevecs += 1
                if prevecs == 3:
                    return True
    return False


def check_win_o(move):
    for i in WIN_KOMBO:
        prevecs = 0
        for j in i:
            if move[j-1] == 'O':
                prevecs += 1
                if prevecs == 3:
                    print('Победа O')
                    return True
    return False






