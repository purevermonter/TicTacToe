import random
import time
import sys

def showboard():
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
    print('-+-+-')
    print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
    print('-+-+-')
    print(board['bl'] + '|' + board['bm'] + '|' + board['br'])
def assignment():
    global board
    board = {'tl':' ', 'tm':' ', 'tr':' ', 'ml':' ', 'mm':' ', 'mr':' ', 'bl':' ', 'bm':' ', 'br':' '}
    print('Determining teams')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('..')
    time.sleep(0.5)
    print('...')
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
    time.sleep(2)
    print('Flipping a coin to determine who goes first')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('..')
    time.sleep(0.5)
    print('...')
    turn = random.randint(0,1)
    if turn == 1:
        print(Pl1 + '\'s turn first')
        theturn(Pl1, p1)
    if turn == 0:
        print(Pl2 + '\'s turn first')
        theturn(Pl2, p2)

def theturn(x, y):
    print ('Where would you like to play '+x+'? (' + y + 's)')
    turn = str(input())
    if turn not in board.keys():
        print('Please type a space code from this chart:')
        print('tl|tm|tr')
        print('--+--+--')
        print('ml|mm|mr')
        print('--+--+--')
        print('bl|bm|br')
        theturn(x, y)
    if board[turn] == ' ':
        board[turn] = str(y)
        showboard()
        checkwin(x)
    else:
        print('Please type an empty square.')
        theturn(x, y)

def checkwin(x):
    if board['tl'] == board['ml'] ==board['bl'] and board['tl']!=' ':
        print(x+' won!')
        again()
    if board['tl'] == board['tm'] ==board['tr'] and board['tl']!=' ':
        print(x+' won!')
        again()
    if board['tr'] == board['mr'] ==board['br'] and board['tr']!=' ':
        print(x+' won!')
        again()
    if board['bl'] == board['bm'] ==board['br'] and board['bl']!=' ':
        print(x+' won!')
        again()
    if board['tl'] == board['mm'] ==board['br'] and board['tl']!=' ':
        print(x+' won!')
        again()
    if board['tr'] == board['mm'] ==board['bl'] and board['tr']!=' ':
        print(x+' won!')
        again()
    if board['tm'] == board['mm'] ==board['bm'] and board['tm']!=' ':
        print(x+' won!')
        again()
    if board['ml'] == board['mm'] ==board['mr'] and board['ml']!=' ':
        print(x+' won!')
        again()
    if ' ' not in board.values():
        again()
    else:
        if x == Pl1:
            theturn(Pl2, p2)
        elif x==Pl2:
            theturn(Pl1, p1)
def again():
    print ('Wanna play again? Type "y" for yes and "n" for no.')
    replay = input()
    if replay == 'y':
        npl()
    elif replay == 'n':
        print('Bye.')
        sys.exit()
    else:
        print('Please type "y" or "n".')
        again()
def npl():
    print ('Same players? Type "y" for yes and "n" for no.')
    play = input()
    if play == 'y':
        assignment()
    elif play == 'n':
        players()
    else:
        print('Please type "y" or "n".')
        npl()
def players():
    print ('Who\'s playing? Type Player 1, press enter, type Player 2, and then press enter again.')
    global Pl1
    global Pl2
    Pl1 = str(input())
    Pl2 = str(input())
    print ('TODAY\'S MATCH: '+Pl1+' VERSUS '+Pl2+'!!')
    assignment()
def welcome():
    print('Welcome to Tic-Tac-Toe.')
    print('To skip intro, enter "skip" now. Otherwise, just press enter when you are ready to continue.')
    skip = input()
    if skip == 'skip':
        players()
    else:
        print('You will be assigned Xs or Os.')
        print('Each turn you will choose what square to play in.')
        input()
        print('Here are the sqare codes:')
        print('tl|tm|tr')
        print('--+--+--')
        print('ml|mm|mr')
        print('--+--+--')
        print('bl|bm|br')
        print('(The first letter is for "top" "middle" or "bottom", the second letter is for "left" "middle" or "right".)')
        input()
        print('Alright, let\'s meet the players...')
        players()
welcome()