# o | x | x
#---+---+---
# o | o | o
#---+---+---
# x | x | x

# Tic Tak Toe wo tukuru

import random

def printPlayer(player):
    print("It's the turn of " + player)

def drowBoard(board):
    print()
    line = " " + board[0] + " | " + board[1] + " | " + board[2] + " "
    line = line.replace("e", " ")
    print(line)

    print("---+---+---")

    line = " " + board[3] + " | " + board[4] + " | " + board[5] + " "
    line = line.replace("e", " ")
    print(line)

    print("---+---+---")

    line = " " + board[6] + " | " + board[7] + " | " + board[8] + " "
    line = line.replace("e", " ")
    print(line)

def askPosition(board, player):
    print("Type your position(1~9):")
    pos = int(input())
    if(board[pos - 1] != "e"  or  not(1 <= pos <= 9)):
        print("Your position is invalid!")
        drowBoard(board)
        printPlayer(player)
        askPosition(board, player)
    return pos

def checkFinish(board):
    # Board is full -> True
    # winner is o/x -> o/x
    # anyone has won -> False

    if not("e" in board):
        return True

    if(board[0] == board[1] == board[2]):
        if(board[0] != "e"):
            return board[0]

    if(board[3] == board[4] == board[5]):
        if(board[3] != "e"):
            return board[3]

    if(board[6] == board[7] == board[8]):
        if(board[6] != "e"):
            return board[6]

    if(board[0] == board[3] == board[6]):
        if(board[0] != "e"):
            return board[0]

    if(board[1] == board[4] == board[7]):
        if(board[1] != "e"):
            return board[1]

    if(board[2] == board[5] == board[8]):
        if(board[2] != "e"):
            return board[2]

    if(board[0] == board[4] == board[8]):
        if(board[0] != "e"):
            return board[0]

    if(board[2] == board[4] == board[6]):
        if(board[2] != "e"):
            return board[2]

    return False

def put(board, pos, mark):
    if(board[pos-1] == "e"):
        board[pos-1] = mark
    else:
        return False

    return board

def whoIsFirst():
    rand = random.randint(0,1)
    if(rand == 0):
        return "o"
    elif(rand == 1):
        return "x"

def turnPlayer(currentPlayer):
    if(currentPlayer == "o"):
        return "x"
    else:
        return "o"

def main():
    e = "e"
    o = "o"
    x = "x"

    board = ["1","2","3","4","5","6","7","8","9"]
    print("Numbers is corresponded like below:")
    drowBoard(board)

    board = [e,e,e,e,e,e,e,e,e]
    player = whoIsFirst()
    isGameFinish = False
    battleState = ""

    while(isGameFinish == False):
        drowBoard(board)
        printPlayer(player)
        pos = int(askPosition(board, player))
        put(board, pos, player)

        battleState = checkFinish(board)
        if(battleState != False):
            isGameFinish = True
        
        player = turnPlayer(player)

    drowBoard(board)
    if(battleState == True):
        print("The board is full!")
    else:
        print(battleState + " has won!")


main()