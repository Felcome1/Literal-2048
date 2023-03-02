
from keyboard import is_pressed, send
import random
from os import system  
import time

l = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
ll = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]

pf = [[0 for i in range(4)] for i in range(4)]
ppf = [[0 for i in range(4)] for i in range(4)]

al = [' ' for i in range(16)]

def rand():

    pf0 = [[1 for i in range(4)] for j in range(4)]
    pf0l = [1 for i in range(16)]
    
    for i in range(16):
        n, n1 = int(i/4), int(i%4)
        if not pf[n][n1]:
            pf0[n][n1] = 0
            pf0l[i] = 0
    
    gr = [i for i in range(16) if not pf0l[i]]

    if len(gr) >= 0:
        r = random.randint(0, len(gr)-1)
        rn = random.randint(0, 100)

        inum = 2 if rn >= 90 else 1
        pf[gr[r]//4][gr[r]%4] = inum

def rewrite_prev_pf():

    for i in range(16):
        n, n1 = int(i/4), int(i%4)
        ppf[n][n1] = pf[n][n1]

def ui():

    passed = False

    b = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]

    for i in range(16):
        
        n, n1 = int(i/4), int(i%4)

        if pf[n][n1] == ppf[n][n1]:
            b[n][n1] = l[pf[n][n1]]

        elif pf[n][n1] != ppf[n][n1] and ppf[n][n1] == 0:
            b[n][n1] = '@' 

        elif pf[n][n1] == ppf[n][n1] + 1 and ppf[n][n1] != 0:
            b[n][n1] = '+' 

        else:
            b[n][n1] = ll[pf[n][n1]]

    

    for i in range(2):

        a = [b[int(i/4)][int(i%4)] for i in range(16)] if not passed else [l[pf[int(i/4)][int(i%4)]] for i in range(16)]
        
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
        print('|        w — up                 |   '+a[0]+'   |   '+a[1]+'   |   '+a[2]+'   |   '+a[3]+'   |                         |')
        print('|        s — down               |       |       |       |       |                         |')
        print('|        a — left                 —————   —————   —————   —————                           |')
        print('|        d — right              |       |       |       |       |                         |')
        print('|        tab - return           |   '+a[4]+'   |   '+a[5]+'   |   '+a[6]+'   |   '+a[7]+'   |                         |')
        print('|        r - restart            |       |       |       |       |                         |')
        print('|                                 —————   —————   —————   —————                           |')
        print('|                               |       |       |       |       |                         |')
        print('|                               |   '+a[8]+'   |   '+a[9]+'   |   '+a[10]+'   |   '+a[11]+'   |                         |')
        print('|                               |       |       |       |       |                         |')
        print('|                                 —————   —————   —————   —————                           |')
        print('|                               |       |       |       |       |                         |')
        print('|                               |   '+a[12]+'   |   '+a[13]+'   |   '+a[14]+'   |   '+a[15]+'   |                         |')
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
        n, n1 = int(i/4), int(i%4)
        pf[n][n1] = ppf[n][n1]
    
    ui()

def move(mvd, mvdr):

    id = [0,1,2,3], [3,2,1,0], [0,0,0,0]
    id1 = [0,1,2,3], [3,2,1,0], [0,0,0,0] 
    triggered = False

    rewrite_prev_pf()

    for i in range(4):

        if pf[id[mvd][2]][id1[mvdr][2]] != 0 or pf[id[mvd][1]][id1[mvdr][1]] != 0 or pf[id[mvd][0]][id1[mvdr][0]] != 0:
            while pf[id[mvd][3]][id1[mvdr][3]] == 0:
                pf[id[mvd][3]][id1[mvdr][3]] = pf[id[mvd][2]][id1[mvdr][2]]
                pf[id[mvd][2]][id1[mvdr][2]] = pf[id[mvd][1]][id1[mvdr][1]]
                pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][0]][id1[mvdr][0]]
                pf[id[mvd][0]][id1[mvdr][0]] = 0
                triggered = True

            if pf[id[mvd][1]][id1[mvdr][1]] != 0 or pf[id[mvd][0]][id1[mvdr][0]] != 0:
                while pf[id[mvd][2]][id1[mvdr][2]] == 0:
                    pf[id[mvd][2]][id1[mvdr][2]] = pf[id[mvd][1]][id1[mvdr][1]]
                    pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][0]][id1[mvdr][0]]
                    pf[id[mvd][0]][id1[mvdr][0]] = 0
                    triggered = True
            
            if pf[id[mvd][0]][id1[mvdr][0]] != 0 and pf[id[mvd][1]][id1[mvdr][1]] == 0:
                pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][0]][id1[mvdr][0]]
                pf[id[mvd][0]][id1[mvdr][0]] = 0
                triggered = True
            

        if pf[id[mvd][3]][id1[mvdr][3]] != 0 and pf[id[mvd][2]][id1[mvdr][2]] != 0:


            if pf[id[mvd][2]][id1[mvdr][2]] == pf[id[mvd][3]][id1[mvdr][3]]:
                pf[id[mvd][3]][id1[mvdr][3]] = pf[id[mvd][3]][id1[mvdr][3]] + 1
                triggered = True
                pf[id[mvd][2]][id1[mvdr][2]] = pf[id[mvd][1]][id1[mvdr][1]]
                pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][0]][id1[mvdr][0]]
                pf[id[mvd][0]][id1[mvdr][0]] = 0

                if pf[id[mvd][1]][id1[mvdr][1]] == pf[id[mvd][2]][id1[mvdr][2]] and pf[id[mvd][2]][id1[mvdr][2]] != 0:
                    pf[id[mvd][2]][id1[mvdr][2]] = pf[id[mvd][2]][id1[mvdr][2]] + 1
                    triggered = True
                    pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][0]][id1[mvdr][0]]
                    pf[id[mvd][0]][id1[mvdr][0]] = 0


            elif pf[id[mvd][1]][id1[mvdr][1]] == pf[id[mvd][2]][id1[mvdr][2]]:
                pf[id[mvd][2]][id1[mvdr][2]] = pf[id[mvd][2]][id1[mvdr][2]] + 1
                triggered = True
                pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][0]][id1[mvdr][0]]
                pf[id[mvd][0]][id1[mvdr][0]] = 0


            elif pf[id[mvd][0]][id1[mvdr][0]] == pf[id[mvd][1]][id1[mvdr][1]] and pf[id[mvd][1]][id1[mvdr][1]] != 0:
                pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][1]][id1[mvdr][1]] + 1
                triggered = True
                pf[id[mvd][0]][id1[mvdr][0]] = 0

        for idc in range(4):
            id[2][idc] += 1
            id1[2][idc] += 1


    system('cls')

    if triggered:

        rand()

    ui()


def retry():

    send('enter')
    system('cls')
    #system('color 07')

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

    if pf == [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]:
        rand()
        rand()

    #system('color E6')
    rewrite_prev_pf()
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
        pf = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
        system('cls')

    else:
        continue
