import random
import time
import sys
import os
aidone = 0
def welcome():
    print('Welcome to Tic-Tac-Toe.')
    print('To skip intro, enter "skip" now. Otherwise, just press enter when you are ready to continue.')
    skip = input()
    if skip == 'skip':
        players()
    else:
        print('You will be assigned Xs or Os. Xs go first, Os go second')
        print('Each turn you will choose what square to play in. (Press enter to continue)')
        input()
        print('Here are the square codes:')
        print('1|2|3')
        print('-+-+-')
        print('4|5|6')
        print('-+-+-')
        print('7|8|9')
        print('(Press enter to continue)')
        input()
        print('Alright, let\'s meet the players...')
        players()

def players():
    global aifiendish, aigenius, ainormal, aifriendly, aizen, aicrazy
    aifiendish = ['[null]', '\\\\REDACTED\\\\', 'bob']
    aigenius = ['Aunt Fanny', 'Cheese Girl', 'HAHAHAHAHA DEATH TO ALL HUMANS']
    ainormal = ['Karl', 'Beepity Boop', 'Abraham "The Emancipator" Lincoln', 'Tic Tac Finger', 'Coco']
    aifriendly = ['b o n k', 'Classic Saltine Crackers', 'Choco Peeb', 'Chris P. Bacon']
    aicrazy = ['Zorpo', 'Patricia', 'Tippy Tap', 'Venison H. Noble', 'Squanchy']
    aizen = ['The Dude', 'Budd', 'Raul', 'Luna', 'Ferb']
    ainametypes = [aizen, aicrazy, aifriendly, ainormal, aigenius, aifiendish]
    print ('Who\'s playing? Type your name, then press enter.')
    global Pl1
    global Pl2
    global PL2
    Pl1 = str(input())
    aichoice = 'sajfksifnngndidisahe'
    print('Choose your difficulty level: 0 is easiest, 5 is hardest. '\
        'Alternatively, just press enter to leave it up to chance')
    choices = ['', '0', '1', '2', '3', '4', '5']
    while aichoice not in choices:
        aichoice = input()
        if aichoice not in choices:
            print('Please type a number (0 through 5) or just press enter')
        elif aichoice == '':
            global PL2
            PL2 = random.choice(random.choice(ainametypes))
        else:
            for x in range (6):
                if int(aichoice) == x:
                    PL2 = random.choice(ainametypes[x])
                    break
    Pl2 = PL2 + ' the AI'
    print ('TODAY\'S MATCH: '+Pl1+' VERSUS '+Pl2+'!!')
    assignment()

def assignment():
    global board
    board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
    print('Determining teams...')
    time.sleep(1.5)
    team = random.randint(0,1)
    if team ==1:
        global p1
        p1 = 'O'
        global p2
        p2 = 'X'
    if team ==0:
        p1 = 'X'
        p2 = 'O'
    print (Pl1+' will be '+p1+'s and '+Pl2+' will be '+p2+'s')
    if team == 0:
        print(Pl1 + '\'s turn first')
        showboard()
        theturn(Pl1, p1)
    if team == 1:
        print(Pl2 + '\'s turn first')
        showboard()
        theturn(Pl2, p2)

def showboard():
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')
    time.sleep(1)

def theturn(x, y):
    if x == Pl1:
        print ('Where would you like to play '+x+'? (' + y + 's)')
        try:
            turn = int(input())
            if turn not in board.keys():
                print('Please type a square code from this chart:')
                print('1|2|3')
                print('-+-+-')
                print('4|5|6')
                print('-+-+-')
                print('7|8|9')
                theturn(x, y)
            if board[turn] == ' ':
                board[turn] = str(y)
                showboard()
                checkwin(x)
            else:
                print('Please type an empty square.')
                theturn(x, y)
        except ValueError:
            print('Please type a square code from this chart:')
            print('1|2|3')
            print('-+-+-')
            print('4|5|6')
            print('-+-+-')
            print('7|8|9')
            theturn(x, y)
    else:
        aiturn()

def aiturn():
    global aidone, aifiendish, aigenius, ainormal, aifriendly, aizen, aicrazy
    aidone = 0
    if aidone == 0 and PL2 in aigenius or PL2 in ainormal or PL2 in aifriendly or PL2 in aifiendish:
        aicheck2()
    if aidone == 0 and PL2 in aigenius or PL2 in ainormal or PL2 in aifriendly:
        aiopener()
    if aidone == 0 and PL2 in aigenius or PL2 in aifiendish:
        aistrat()
    if aidone == 0 and PL2 in aizen or PL2 in aifriendly:
        aizenn()
    if aidone == 0 and PL2 in PL2 in aigenius or PL2 in ainormal or PL2 in aifiendish or PL2 in aicrazy:
        aicrazyy()

def aiopener():
    if board[5] == ' ':
        aiout(5)

def aizenn():
    global board
    for ai in list(board.keys()):
        if board[ai] == p2:
                continue
        elif board[ai] == p1:
            continue
        else:
            aiout(ai)
            break

def aicrazyy():
    global board
    while True:
        ai = random.randint(1, 9)
        if board[ai] == p2:
                continue
        elif board[ai] == p1:
            continue
        else:
            aiout(ai)
            break

def aistrat():
    def win(x):
        if x == 1:
            return [1, 2, 3]
        if x == 2:
            return [4, 5, 6]
        if x == 3:
            return [7, 8, 9]
        if x == 4:
            return [1, 4, 7]
        if x == 5:
            return [2, 5, 8]
        if x == 6:
            return [3, 6, 9]
        if x == 7:
            return [1, 5, 9]
        if x == 8:
            return [3, 5, 7]
    fives = [2, 5, 7, 8]
    if PL2 in aifiendish:
        if board[5] == p1 and board[1] == p2\
        and (board[7] == p1 or board[3] == p1) and board[9] == p2:
            if board[7] == p1:
                aiout(3)
            elif board [3] == p1:
                aiout(7)
        elif board[5] == p1 and board[1] == p2\
        and board[7] == ' ' and board[3] == ' ' and board[9] == ' ':
            aiout(9)
        elif board[5] == p1 and board[9] == p1:
            aicrazyy()
        elif board[1] == ' ':
            aiout(1)
    if board[5] == p2:
        poss = [1, 2, 3, 4, 6, 7, 8, 9]
        for x in fives:
            if board[(win(x))[0]] == ' ' and board[(win(x))[2]] == ' ':
                for y in range(1, 9):
                    if board[(win(y)[0])] or board[(win(y)[1])] or board[(win(y)[2])] == p2 and \
                        board[(win(y)[0])] and board[(win(y)[1])] and board[(win(y)[2])] != p1:
                            for b in range (1, 9):
                                if b in win(y) and b in win(x):
                                    aiout(b)
                    if y not in fives:
                        if board[(win(y)[0])] and board[(win(y)[1])] and board[(win(y)[2])] != p1:
                            for b in range (1, 9):
                                if b in win(y) and b in win(x):
                                    aiout(b)
    else:
        aicrazyy()
def aicheck2():
    global aidone
    pll = [p2, p1]
    for x in pll:
        if x == p1 and Pl2 in aifriendly:
            break
        for ai in list(board.keys()):
            ail = ai-1
            aill = ai-2
            air = ai+1
            airr = ai+2
            aiu = ai-3
            aiuu = ai-6
            aid = ai+3
            aidd = ai+6
            aidi1 = ai - 4
            aidi2 = ai +4
            aidi3 = ai -2
            aidi4 = ai + 2
            def check2(a, b, c, b1, b2, pl):
                if (ai == a or ai == b or ai == c) and board[b1] == pl and board[b2] == pl:
                    return True
            def check2d(a, b1, b2, pl):
                if ai == a and board[b1] == pl and board[b2] == pl:
                    return True
            if board[ai] == p2:
                continue
            elif board[ai] == p1:
                continue
            if check2(2, 5, 8, ail, air, x):
                aiout(ai)
                break
            elif check2(4, 5, 6, aiu, aid, x):
                aiout(ai)
                break
            elif check2(1, 2, 3, aid, aidd, x):
                aiout(ai)
                break
            elif check2(7, 8, 9, aiu, aiuu, x):
                aiout(ai)
                break
            elif check2(1, 4, 7, air, airr, x):
                aiout(ai)
                break
            elif check2(3, 6, 9, ail, aill, x):
                aiout(ai)
                break
            elif check2d(5, aidi1, aidi2, x):
                aiout(ai)
                break
            elif check2d(5, aidi3, aidi4, x):
                aiout(ai)
            elif check2d(1, 5, 9, x):
                aiout(ai)
            elif check2d(3, 5, 7, x):
                aiout(ai)
            elif check2d(7, 3, 5, x):
                aiout(ai)
            elif check2d(9, 1, 5, x):
                aiout(ai)
                break
        if aidone == 1:
            break

def aiout(x):
    board[x] = p2
    print (Pl2 + ' played here: ('+p2+'s)')
    showboard()
    global aidone
    aidone = 1
    checkwin(Pl2)

def checkwin(x):
    for y in list(board.keys()):
        l = int(y-1)
        r = int(y+1)
        u = int(y-3)
        d = int(y+3)
        if y == 2 or y == 5 or y == 8:
            if board[y] == board[l] ==board[r] and board[y]!=' ':
                print(x+' won!')
                again()
        if y== 4 or y == 5 or y == 6:
            if board[y] == board[u] ==board[d] and board[y]!=' ':
                print(x+' won!')
                again()
    if board[5] == board[1] ==board[9] and board[5]!=' ':
        print(x+' won!')
        again()
    elif board[5] == board[3] ==board[7] and board[5]!=' ':
        print(x+' won!')
        again()
    elif ' ' not in board.values():
        print('That\'s a draw.')
        again()
    else:
        if x == Pl1:
            theturn(Pl2, p2)
        elif x==Pl2:
            theturn(Pl1, p1)
def again():
    print ('Wanna play again? Type "y" for yes and "n" for no.')
    replay = 'asdfjrvrnr;vrnvr;n;vrn;nr'
    while replay != ('y' or 'n'):
        replay = input()
        if replay == 'y':
            npl()
        elif replay == 'n':
            print('Bye.')
            os._exit(1)
        else:
            print('Please type "y" or "n".')
def npl():
    print ('Same players? Type "y" for yes and "n" for no.')
    play = 'sadfjrhfuruifivivvvvvvvv'
    while play != ('y' or 'n'):
        play = input()
        if play == 'y':
            assignment()
        elif play == 'n':
            players()
        else:
            print('Please type "y" or "n".')

welcome()
