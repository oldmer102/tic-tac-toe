import check
import bot


prefect = False
pole = f"""{check.START[0]} | {check.START[1]} | {check.START[2]}\n{check.START[3]} | {check.START[4]} | {check.START[5]}\n{check.START[6]} | {check.START[7]} | {check.START[8]}\n"""
print('Для хода введите номер поля, куда вы хотите поставить Х\n' + pole)

while not prefect:
    num = None
    while not check.check_mistake(num):
        num = input('Введите номер поля: ')
    move = check.set_vell(num)
    move = bot.bot_tic_tac(move)
    pole = f"""{move[0]} | {move[1]} | {move[2]}\n{move[3]} | {move[4]} | {move[5]}\n{move[6]} | {move[7]} | {move[8]}\n"""
    print(pole)
    prefect = check.check_win_x(move) or check.check_win_o(move)


