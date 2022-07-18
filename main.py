''' Как играть: есть поле 3х3, для заполнения вводить 0,0 и ваше значение поставится в вверхнем левом углу.
 Отсёт полей идёт с лева направо, сверху вниз, а так же отсёт начинается с 0'''
import check
import random
from check import zapolnenie
from check import prevecs

def check_mistake(num:list):
    if len(num) == 2:
        a = num[0]
        b = num[1]
        if zapolnenie[a][b] == '-':
            zapolnenie[a][b] = 'X'
        else:
            print('Вы ввели неправильное значение')
def bot_tic_tac():
    c = False
    while c == False:
        num_1 = random.randint(0, 2)
        num_2 = random.randint(0, 2)
        if zapolnenie[num_1][num_2] == '-':
            zapolnenie[num_1][num_2] = 'O'
            c = True
while prevecs > 2:
    b = input('Введите поле: ')
    b = b.split(sep=',')
    b = map(int, b)
    check_mistake(list(b))
    bot_tic_tac()
    pole = f"""{zapolnenie[0][0]} | {zapolnenie[0][1]} | {zapolnenie[0][2]}\n{zapolnenie[1][0]} | {zapolnenie[1][1]} | {zapolnenie[1][2]}\n{zapolnenie[2][0]} | {zapolnenie[2][1]} | {zapolnenie[2][2]}\n"""
    print(pole)
    b = check.check_victory(zapolnenie)
    if b == 1:
        prevecs = b



