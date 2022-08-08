import keyboard
from keyboard import is_pressed as press
import random
from os import system  
import time

l = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
ll = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
pf = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
     ]
ppf = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
     ]
al = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',]

def rand():

    pf0 = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    ]
    pf0l = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    q = 0
    def ec():
        e = 0
        while e != 4:
            if pf[q][e] == 0:
                pf0[q][e] = 0
                pf0l[q*4+e] = 0
            else:
                pass
            e += 1
    while q != 4:
        ec() # Seems cycle in cycle doesn't work, so here's a function
        q += 1
    c = 0 
    gr = []
    while c != 16:
        if pf0l[c] == 0:
            gr.append(c)
        else:
            pass
        c += 1
    if len(gr) >= 0:
        r = random.randint(0, len(gr)-1)
        rn = random.randint(0, 100)
        if rn >= 90:
            inum = 2
        else:
            inum = 1
        pf[gr[r]//4][gr[r]%4] = inum
    else:
        pass

def prbe():
    q = 0
    def ec2():
        e = 0
        while e != 4:
            ppf[e][q] = pf[e][q]
            e+=1
    while q != 4:
        ec2()
        q+=1

def ui():
    b = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    ii = 0
    def icounter():
        i = 0
        while i != 4:
            if pf[ii][i] == ppf[ii][i]:
                b[ii][i] = l[pf[ii][i]]
            elif pf[ii][i] != ppf[ii][i] and ppf[ii][i] == 0:
                b[ii][i] = '@' 
            elif pf[ii][i] == ppf[ii][i] + 1 and ppf[ii][i] != 0:
                b[ii][i] = '+' 
            else:
                b[ii][i] = ll[pf[ii][i]]
            i += 1
    while ii != 4:
        icounter()
        ii += 1
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
    print('|        w — up                 |   '+b[0][0]+'   |   '+b[0][1]+'   |   '+b[0][2]+'   |   '+b[0][3]+'   |                         |')
    print('|        s — down               |       |       |       |       |                         |')
    print('|        a — left                 —————   —————   —————   —————                           |')
    print('|        d — right              |       |       |       |       |                         |')
    print('|        tab - return           |   '+b[1][0]+'   |   '+b[1][1]+'   |   '+b[1][2]+'   |   '+b[1][3]+'   |                         |')
    print('|        r - restart            |       |       |       |       |                         |')
    print('|                                 —————   —————   —————   —————                           |')
    print('|                               |       |       |       |       |                         |')
    print('|                               |   '+b[2][0]+'   |   '+b[2][1]+'   |   '+b[2][2]+'   |   '+b[2][3]+'   |                         |')
    print('|                               |       |       |       |       |                         |')
    print('|                                 —————   —————   —————   —————                           |')
    print('|                               |       |       |       |       |                         |')
    print('|                               |   '+b[3][0]+'   |   '+b[3][1]+'   |   '+b[3][2]+'   |   '+b[3][3]+'   |                         |')
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
    time.sleep(0.18)
    system('cls')
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
    print('|                               |  '+al[0]*3+'  |  '+al[0]*3+'  |  '+al[0]*3+'  |  '+al[0]*3+'  |                         |')
    print('|        w — up                 |   '+l[pf[0][0]]+'   |   '+l[pf[0][1]]+'   |   '+l[pf[0][2]]+'   |   '+l[pf[0][3]]+'   |                         |')
    print('|        s — down               |       |       |       |       |                         |')
    print('|        a — left                 —————   —————   —————   —————                           |')
    print('|        d — right              |       |       |       |       |                         |')
    print('|        tab - return           |   '+l[pf[1][0]]+'   |   '+l[pf[1][1]]+'   |   '+l[pf[1][2]]+'   |   '+l[pf[1][3]]+'   |                         |')
    print('|        r - restart            |       |       |       |       |                         |')
    print('|                                 —————   —————   —————   —————                           |')
    print('|                               |       |       |       |       |                         |')
    print('|                               |   '+l[pf[2][0]]+'   |   '+l[pf[2][1]]+'   |   '+l[pf[2][2]]+'   |   '+l[pf[2][3]]+'   |                         |')
    print('|                               |       |       |       |       |                         |')
    print('|                                 —————   —————   —————   —————                           |')
    print('|                               |       |       |       |       |                         |')
    print('|                               |   '+l[pf[3][0]]+'   |   '+l[pf[3][1]]+'   |   '+l[pf[3][2]]+'   |   '+l[pf[3][3]]+'   |                         |')
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
def turnback():
    q = 0
    def ec1():
        e = 0
        while e != 4:
            pf[e][q] = ppf[e][q]
            e+=1
    while q != 4:
        ec1()
        q+=1
    ui()

def move(mvd, mvdr):
    i = 0
    id = [0,1,2,3], [3,2,1,0], [0,0,0,0]
    id1 = [0,1,2,3], [3,2,1,0], [0,0,0,0] 
    mmt = False
    prbe()
    while i!=4:
        if pf[id[mvd][2]][id1[mvdr][2]] != 0 or pf[id[mvd][1]][id1[mvdr][1]] != 0 or pf[id[mvd][0]][id1[mvdr][0]] != 0:
            while pf[id[mvd][3]][id1[mvdr][3]] == 0:
                pf[id[mvd][3]][id1[mvdr][3]] = pf[id[mvd][2]][id1[mvdr][2]]
                pf[id[mvd][2]][id1[mvdr][2]] = pf[id[mvd][1]][id1[mvdr][1]]
                pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][0]][id1[mvdr][0]]
                pf[id[mvd][0]][id1[mvdr][0]] = 0
                mmt = True
            if pf[id[mvd][1]][id1[mvdr][1]] != 0 or pf[id[mvd][0]][id1[mvdr][0]] != 0:
                while pf[id[mvd][2]][id1[mvdr][2]] == 0:
                    pf[id[mvd][2]][id1[mvdr][2]] = pf[id[mvd][1]][id1[mvdr][1]]
                    pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][0]][id1[mvdr][0]]
                    pf[id[mvd][0]][id1[mvdr][0]] = 0
                    mmt = True
            else:
                pass
            if pf[id[mvd][0]][id1[mvdr][0]] != 0 and pf[id[mvd][1]][id1[mvdr][1]] == 0:
                pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][0]][id1[mvdr][0]]
                pf[id[mvd][0]][id1[mvdr][0]] = 0
                mmt = True
        else:
            pass
        if pf[id[mvd][3]][id1[mvdr][3]] != 0 and pf[id[mvd][2]][id1[mvdr][2]] != 0:
            if pf[id[mvd][2]][id1[mvdr][2]] == pf[id[mvd][3]][id1[mvdr][3]]:
                pf[id[mvd][3]][id1[mvdr][3]] = pf[id[mvd][3]][id1[mvdr][3]] + 1
                mmt = True
                pf[id[mvd][2]][id1[mvdr][2]] = pf[id[mvd][1]][id1[mvdr][1]]
                pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][0]][id1[mvdr][0]]
                pf[id[mvd][0]][id1[mvdr][0]] = 0
                if pf[id[mvd][1]][id1[mvdr][1]] == pf[id[mvd][2]][id1[mvdr][2]] and pf[id[mvd][2]][id1[mvdr][2]] != 0:
                    pf[id[mvd][2]][id1[mvdr][2]] = pf[id[mvd][2]][id1[mvdr][2]] + 1
                    mmt = True
                    pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][0]][id1[mvdr][0]]
                    pf[id[mvd][0]][id1[mvdr][0]] = 0
            elif pf[id[mvd][1]][id1[mvdr][1]] == pf[id[mvd][2]][id1[mvdr][2]]:
                pf[id[mvd][2]][id1[mvdr][2]] = pf[id[mvd][2]][id1[mvdr][2]] + 1
                mmt = True
                pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][0]][id1[mvdr][0]]
                pf[id[mvd][0]][id1[mvdr][0]] = 0
            elif pf[id[mvd][0]][id1[mvdr][0]] == pf[id[mvd][1]][id1[mvdr][1]] and pf[id[mvd][1]][id1[mvdr][1]] != 0:
                pf[id[mvd][1]][id1[mvdr][1]] = pf[id[mvd][1]][id1[mvdr][1]] + 1
                mmt = True
                pf[id[mvd][0]][id1[mvdr][0]] = 0
        else:
            pass
        i += 1
        idc = 0
        while idc != 4:
            id[2][idc] += 1
            id1[2][idc] += 1
            idc += 1
    system('cls')
    if mmt == True:
        rand()
    else:
        pass
    ui()

def retry():
    system('cls')
    system('color 07')
    while True:
        let = input('Wanna try again?\n Y - yes    N - no\n/=\  \n' + ' ')
        if let == 'Y':
            system('cls')
            ui()
            return(True)
        elif let == 'N':
            system('cls')
            ui()
            return(False)
        else:
            system('cls')
            pass
            
while True:
    if pf == [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]:
        rand()
        rand()
    system('color E6')
    prbe()
    ui()
    while True:
        if press('w'):
            move(1, 2)
            time.sleep(0)
            pass
        elif press('a'):
            move(2, 1)
            time.sleep(0)
            pass
        elif press('s'):
            move(0, 2)
            time.sleep(0)
            pass
        elif press('d'):
            move(2, 0)
            time.sleep(0)
            pass
        elif press('r'):
            break
        elif press('tab'):
            turnback()
            time.sleep(0)
            pass
    if retry() == True:
        pf = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
        system('cls')
        pass
    else:
        continue