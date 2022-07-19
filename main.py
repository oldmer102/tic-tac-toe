import check
import bot



prefect = False
prever = 0
bot_or_player = None


while not check.check_plaers(bot_or_player):
    bot_or_player = input('1 или 2 игрока? ')

#Один игрок
if int(bot_or_player) == 1:
    pole = f"""{check.START[0]} | {check.START[1]} | {check.START[2]}\n{check.START[3]} | {check.START[4]} | {check.START[5]}\n{check.START[6]} | {check.START[7]} | {check.START[8]}\n"""
    print('Для хода введите номер поля, куда вы хотите поставить Х\n' + pole)
    while not prefect:
        num = None
        while not check.check_mistake(num):
            num = input('Введите номер поля: ')
        move = check.set_vell(num)
        if check.check_win_x(move):
            pole = f"""{move[0]} | {move[1]} | {move[2]}\n{move[3]} | {move[4]} | {move[5]}\n{move[6]} | {move[7]} | {move[8]}\n"""
            print(pole + '\nпобеда X')
            break
        if check.check_win_o(move):
            pole = f"""{move[0]} | {move[1]} | {move[2]}\n{move[3]} | {move[4]} | {move[5]}\n{move[6]} | {move[7]} | {move[8]}\n"""
            print(pole + '\nпобеда O')
            break

        if check.has_free(move, prever):
            pole = f"""{move[0]} | {move[1]} | {move[2]}\n{move[3]} | {move[4]} | {move[5]}\n{move[6]} | {move[7]} | {move[8]}\n"""
            print(pole)
            print('Ничья!')
            break
        move = bot.bot_tic_tac(move)
        pole = f"""{move[0]} | {move[1]} | {move[2]}\n{move[3]} | {move[4]} | {move[5]}\n{move[6]} | {move[7]} | {move[8]}\n"""
        print(pole)
        prefect = check.check_win_x(move) or check.check_win_o(move)

#Два игрока
if int(bot_or_player) == 2:
    pole = f"""{check.START[0]} | {check.START[1]} | {check.START[2]}\n{check.START[3]} | {check.START[4]} | {check.START[5]}\n{check.START[6]} | {check.START[7]} | {check.START[8]}\n"""
    print('Для хода введите номер поля, куда вы хотите поставить Х, первым ходит X потом O\n' + pole)
    while not prefect:
        num = None
        while not check.check_mistake(num):
            num = input('Введите номер поля: ')
        move = check.set_vell(num)
        if check.check_win_x(move):
            pole = f"""{move[0]} | {move[1]} | {move[2]}\n{move[3]} | {move[4]} | {move[5]}\n{move[6]} | {move[7]} | {move[8]}\n"""
            print(pole + '\nпобеда X')
            break

        if check.has_free(move, prever):
            pole = f"""{move[0]} | {move[1]} | {move[2]}\n{move[3]} | {move[4]} | {move[5]}\n{move[6]} | {move[7]} | {move[8]}\n"""
            print(pole)
            print('Ничья!')
            break

        pole = f"""{move[0]} | {move[1]} | {move[2]}\n{move[3]} | {move[4]} | {move[5]}\n{move[6]} | {move[7]} | {move[8]}\n"""
        print(pole)
        prefect = check.check_win_x(move) or check.check_win_o(move)
        num = None
        while not check.check_mistake(num):
            num = input('Введите номер поля: ')
        move = check.set_vell(num, posit='O')
        pole = f"""{move[0]} | {move[1]} | {move[2]}\n{move[3]} | {move[4]} | {move[5]}\n{move[6]} | {move[7]} | {move[8]}\n"""
        print(pole)
        prefect = check.check_win_x(move) or check.check_win_o(move)

