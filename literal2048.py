from keyboard import is_pressed, send
import random
from os import system
import time

l = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
     'W', 'X', 'Y', 'Z']
l_lo = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
      'w', 'x', 'y', 'z']

board = [[0 for i in range(4)] for i in range(4)]
prev_board = [[0 for i in range(4)] for i in range(4)]

def rand():

    ll_board_bool = [[1 for i in range(4)] for j in range(4)]
    l_board_bool = [1 for i in range(16)]

    for field in range(16):
        y, x = int(field / 4), int(field % 4)
        if not board[y][x]:
            ll_board_bool[y][x] = 0
            l_board_bool[field] = 0

    free_field = [field for field in range(16) if not l_board_bool[field]]

    if len(free_field) >= 0:

        rand_field = random.randint(0, len(free_field) - 1)
        val = 2 if random.randint(0, 100) >= 90 else 1
        board[free_field[rand_field] // 4][free_field[rand_field] % 4] = val


def save_board():

    for i in range(16):
        y, x = int(i / 4), int(i % 4)
        prev_board[y][x] = board[y][x]


def ui():

    passed = False
    board_anim = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]

    for f_index in range(16):

        y, x = int(f_index / 4), int(f_index % 4)

        if board[y][x] == prev_board[y][x]:
            board_anim[y][x] = l[board[y][x]]

        elif board[y][x] != prev_board[y][x] and prev_board[y][x] == 0:
            board_anim[y][x] = '@'

        elif board[y][x] == prev_board[y][x] + 1 and prev_board[y][x] != 0:
            board_anim[y][x] = '+'

        else:
            board_anim[y][x] = l_lo[board[y][x]]

    for i in range(2):
        a = [board_anim[int(i / 4)][int(i % 4)] for i in range(16)] if not passed else [l[board[int(i / 4)][int(i % 4)]] for i in
                                                                               range(16)]

        print('  ———————————————————————————————————————————————————————————————————————————————————————  ')
        print('|                                                                                         |')
        print('|                                                                                         |')
        print('|                          ####        #####         ##       ###                         |')
        print('|                        ##    ##     #     #       # #      #   #                        |')
        print('|                              ##     #     #      #  #       ###                         |')
        print('|                            ##       #     #     ######     #   #                        |')
        print('|                          ##         #     #         #      #   #                        |')
        print('|                        ########      #####          #       ###                         |')
        print('|                                                                                         |')
        print('|                                                                                         |')
        print('|                                 —————   —————   —————   —————                           |')
        print('|                               |       |       |       |       |                         |')
        print('|        w — up                 |   ' + a[0] + '   |   ' + a[1] + '   |   ' + a[2] + '   |   ' + a[
            3] + '   |                         |')
        print('|        s — down               |       |       |       |       |                         |')
        print('|        a — left                 —————   —————   —————   —————                           |')
        print('|        d — right              |       |       |       |       |                         |')
        print('|        tab - return           |   ' + a[4] + '   |   ' + a[5] + '   |   ' + a[6] + '   |   ' + a[
            7] + '   |                         |')
        print('|        r - restart            |       |       |       |       |                         |')
        print('|                                 —————   —————   —————   —————                           |')
        print('|                               |       |       |       |       |                         |')
        print('|                               |   ' + a[8] + '   |   ' + a[9] + '   |   ' + a[10] + '   |   ' + a[
            11] + '   |                         |')
        print('|                               |       |       |       |       |                         |')
        print('|                                 —————   —————   —————   —————                           |')
        print('|                               |       |       |       |       |                         |')
        print('|                               |   ' + a[12] + '   |   ' + a[13] + '   |   ' + a[14] + '   |   ' + a[
            15] + '   |                         |')
        print('|                               |       |       |       |       |                         |')
        print('|                                 —————   —————   —————   —————                           |')
        print('|                                                                                         |')
        print('|                                                                                         |')
        print('|                                                                                         |')
        print('|                                                                                         |')
        print('|                                                                                         |')
        print('|                                                                                         |')
        print("|                                                                                         |")
        print('  ———————————————————————————————————————————————————————————————————————————————————————  ')

        if not passed:
            time.sleep(0.18)
            system('cls')

        passed = True

def turnback():

    for i in range(16):
        n, n1 = int(i / 4), int(i % 4)
        board[n][n1] = prev_board[n][n1]

    ui()


def move(dir_y, dir_x):

    index_y = [0, 1, 2, 3], [3, 2, 1, 0], [0, 0, 0, 0]
    index_x = [0, 1, 2, 3], [3, 2, 1, 0], [0, 0, 0, 0]
    triggered = False

    save_board()

    for i in range(4):

        if board[index_y[dir_y][2]][index_x[dir_x][2]] != 0 or board[index_y[dir_y][1]][index_x[dir_x][1]] != 0 or board[index_y[dir_y][0]][index_x[dir_x][0]] != 0:
            while board[index_y[dir_y][3]][index_x[dir_x][3]] == 0:
                board[index_y[dir_y][3]][index_x[dir_x][3]] = board[index_y[dir_y][2]][index_x[dir_x][2]]
                board[index_y[dir_y][2]][index_x[dir_x][2]] = board[index_y[dir_y][1]][index_x[dir_x][1]]
                board[index_y[dir_y][1]][index_x[dir_x][1]] = board[index_y[dir_y][0]][index_x[dir_x][0]]
                board[index_y[dir_y][0]][index_x[dir_x][0]] = 0
                triggered = True

            if board[index_y[dir_y][1]][index_x[dir_x][1]] != 0 or board[index_y[dir_y][0]][index_x[dir_x][0]] != 0:
                while board[index_y[dir_y][2]][index_x[dir_x][2]] == 0:
                    board[index_y[dir_y][2]][index_x[dir_x][2]] = board[index_y[dir_y][1]][index_x[dir_x][1]]
                    board[index_y[dir_y][1]][index_x[dir_x][1]] = board[index_y[dir_y][0]][index_x[dir_x][0]]
                    board[index_y[dir_y][0]][index_x[dir_x][0]] = 0
                    triggered = True

            if board[index_y[dir_y][0]][index_x[dir_x][0]] != 0 and board[index_y[dir_y][1]][index_x[dir_x][1]] == 0:
                board[index_y[dir_y][1]][index_x[dir_x][1]] = board[index_y[dir_y][0]][index_x[dir_x][0]]
                board[index_y[dir_y][0]][index_x[dir_x][0]] = 0
                triggered = True

        if board[index_y[dir_y][3]][index_x[dir_x][3]] != 0 and board[index_y[dir_y][2]][index_x[dir_x][2]] != 0:

            if board[index_y[dir_y][2]][index_x[dir_x][2]] == board[index_y[dir_y][3]][index_x[dir_x][3]]:
                board[index_y[dir_y][3]][index_x[dir_x][3]] = board[index_y[dir_y][3]][index_x[dir_x][3]] + 1
                triggered = True
                board[index_y[dir_y][2]][index_x[dir_x][2]] = board[index_y[dir_y][1]][index_x[dir_x][1]]
                board[index_y[dir_y][1]][index_x[dir_x][1]] = board[index_y[dir_y][0]][index_x[dir_x][0]]
                board[index_y[dir_y][0]][index_x[dir_x][0]] = 0

                if board[index_y[dir_y][1]][index_x[dir_x][1]] == board[index_y[dir_y][2]][index_x[dir_x][2]] and board[index_y[dir_y][2]][index_x[dir_x][2]] != 0:
                    board[index_y[dir_y][2]][index_x[dir_x][2]] = board[index_y[dir_y][2]][index_x[dir_x][2]] + 1
                    triggered = True
                    board[index_y[dir_y][1]][index_x[dir_x][1]] = board[index_y[dir_y][0]][index_x[dir_x][0]]
                    board[index_y[dir_y][0]][index_x[dir_x][0]] = 0


            elif board[index_y[dir_y][1]][index_x[dir_x][1]] == board[index_y[dir_y][2]][index_x[dir_x][2]]:
                board[index_y[dir_y][2]][index_x[dir_x][2]] = board[index_y[dir_y][2]][index_x[dir_x][2]] + 1
                triggered = True
                board[index_y[dir_y][1]][index_x[dir_x][1]] = board[index_y[dir_y][0]][index_x[dir_x][0]]
                board[index_y[dir_y][0]][index_x[dir_x][0]] = 0


            elif board[index_y[dir_y][0]][index_x[dir_x][0]] == board[index_y[dir_y][1]][index_x[dir_x][1]] and board[index_y[dir_y][1]][index_x[dir_x][1]] != 0:
                board[index_y[dir_y][1]][index_x[dir_x][1]] = board[index_y[dir_y][1]][index_x[dir_x][1]] + 1
                triggered = True
                board[index_y[dir_y][0]][index_x[dir_x][0]] = 0

        for index in range(4):
            index_y[2][index] += 1
            index_x[2][index] += 1

    system('cls')

    if triggered:
        rand()

    ui()


def retry():
    send('enter')
    system('cls')
    # system('color 07')

    while True:

        let = input('Wanna try again?\n Y - yes    N - no\n/=\  \n' + ' ').capitalize()

        if let == 'Y':
            system('cls')
            ui()
            return True

        elif let == 'N':
            system('cls')
            ui()
            return False

        else:
            system('cls')


while True:

    if board == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]:
        rand()
        rand()

    # system('color E6')
    save_board()
    ui()

    while True:

        if is_pressed('w'):
            move(1, 2)

        elif is_pressed('a'):
            move(2, 1)

        elif is_pressed('s'):
            move(0, 2)

        elif is_pressed('d'):
            move(2, 0)

        elif is_pressed('r'):
            break

        elif is_pressed('tab'):
            turnback()

    if retry() == True:
        board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        system('cls')

    else:
        continue
