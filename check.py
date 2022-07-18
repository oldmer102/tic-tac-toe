zapolnenie = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
prevecs = 3
def check_mistake(a,pole:list):
    a = pole
    if a == '-':
        return True

def check_victory(a):
    if a[0][0] == 'X':
        if a[0][1] == 'X':
            if a[0][2] == 'X':
                print('Победа Х')
                return 1
        if a[1][0] == 'X':
            if a[2][0] == 'X':
                print('Победа Х')
                return 1
        if a[1][1] == 'X':
            if a[2][2] == 'X':
                print('Победа Х')
                return 1
    if a[0][1] == 'X':
        if a[1][1] == 'X':
            if a[2][1] == 'X':
                print('Победа Х')
                return 1
    if a[0][2] == 'X':
        if a[1][2] == 'X':
            if a[0][2] == 'X':
                print('Победа Х')
                return 1
        if a[1][1] == 'X':
            if a[2][0] == 'X':
                print('Победа Х')
                return 1
    if a[1][0] == 'X':
        if a[1][1] == 'X':
            if a[1][2] == 'X':
                print('Победа Х')
                return 1
    if a[2][0] == 'X':
        if a[2][1] == 'X':
            if a[2][2] == 'X':
                print('Победа Х')
                return 1
    if a[0][0] == 'O':
        if a[0][1] == 'O':
            if a[0][2] == 'O':
                print('Победа O')
                return 1
        if a[1][0] == 'O':
            if a[2][0] == 'O':
                print('Победа O')
                return 1
        if a[1][1] == 'O':
            if a[2][2] == 'O':
                print('Победа O')
                return 1
    if a[0][1] == 'O':
        if a[1][1] == 'O':
            if a[2][1] == 'O':
                print('Победа O')
                return 1
    if a[0][2] == 'O':
        if a[1][2] == 'O':
            if a[0][2] == 'O':
                print('Победа O')
                return 1
        if a[1][1] == 'O':
            if a[2][0] == 'O':
                print('Победа O')
                return 1
    if a[1][0] == 'O':
        if a[1][1] == 'O':
            if a[1][2] == 'O':
                print('Победа O')
                return 1
    if a[2][0] == 'O':
        if a[2][1] == 'O':
            if a[2][2] == 'O':
                print('Победа O')
                return 1




