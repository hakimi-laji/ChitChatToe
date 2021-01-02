#TICTACTOE SINGLEPLAYER

theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = str(input('>>> '))
    
    if theBoard[move] == ' ':
        theBoard[move] = turn
    else:
        print ('Error')
    
    #check win status
    if theBoard['1'] == turn and theBoard['2'] == turn and theBoard['3'] == turn:
        print (turn + " is the winner")
        break
    elif theBoard['4'] == turn and theBoard['5'] == turn and theBoard['6'] == turn:
        print (turn + " is the winner")
        break
    elif theBoard['7'] == turn and theBoard['8'] == turn and theBoard['9'] == turn:
        print (turn + " is the winner")
        break
    elif theBoard['1'] == turn and theBoard['4'] == turn and theBoard['7'] == turn:
        print (turn + " is the winner")
        break
    elif theBoard['2'] == turn and theBoard['5'] == turn and theBoard['8'] == turn:
        print (turn + " is the winner")
        break
    elif theBoard['3'] == turn and theBoard['6'] == turn and theBoard['9'] == turn:
        print (turn + " is the winner")
        break
    elif theBoard['1'] == turn and theBoard['5'] == turn and theBoard['9'] == turn:
        print (turn + " is the winner")
        break
    elif theBoard['3'] == turn and theBoard['5'] == turn and theBoard['7'] == turn:
        print (turn + " is the winner")
        break
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

printBoard(theBoard)
