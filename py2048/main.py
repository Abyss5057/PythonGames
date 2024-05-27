# +-------+-------+-------+-------+
# |       |       |       |       |
# |  1024 |   128 |   256 |     2 |
# |       |       |       |       |
# +-------+-------+-------+-------+
# |       |       |       |       |
# |  1024 |   128 |   256 |     2 |
# |       |       |       |       |
# +-------+-------+-------+-------+
# |       |       |       |       |
# |  1024 |   128 |   256 |     2 |
# |       |       |       |       |
# +-------+-------+-------+-------+
# |       |       |       |       |
# |  1024 |   128 |   256 |     2 |
# |       |       |       |       |
# +-------+-------+-------+-------+
# making 2048 in python!
# 表示が崩れてしまうため、等幅フォントの使用を強く推奨します

"""
todo:
 新たにできたタイルにハイライト
 数字が大きいものにカラーリング
 undo機能の実装
"""

import random
import os
import sys

osName = ""

char_tate = "|"
char_yoko = "-"
char_cross = "+"
char_space = " "

SCORE = 0
STEP = 0

isZeroDelete = 1
initTileNum = 2


DEBUG_BOARD = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


def getOS():
    global osName
    osType = os.name

    if(osType == "nt"):
        osName = "windows"
    elif(osType == "posix"):
        osName = "unix"

def consoleClear():
    global osName

    if(osName == "windows"):
        os.system("cls")
    elif(osName == "unix"):
        os.system("clear")

def allListEqual(li):
    for i in li:
        if(li[0] != i):
            return False
    
    return True

def makeYokosen(char1, char2, boardLine = [-1, -1, -1, -1]):
    # this function returns yokosen.
    #      +------+------+------+------+
    # char 12222221222222122222212222221

    line = ""

    if(boardLine[0] == -1):
        for i in range(4):
            line += char1
            for j in range(7):
                line += char2

    else:
        for i in range(4):
            num = boardLine[i]
            digit = len(str(num))

            line += char1
            for j in range(6 - digit):
                line += char2
            line += str(num)
            line += char2
        

    line += char1

    return line

def makeNumLine(boardLine):
    # boardLine = [128, 4, 64, 0]
    line = makeYokosen(char_tate, char_space, boardLine)
    if(isZeroDelete == 1):
        line = line.replace(" 0 ", "   ")
    return line

def drow(board, score, step, newPos = [-1, -1]):
    line_kugiri = makeYokosen(char_cross, char_yoko)
    line_blank = makeYokosen(char_tate, char_space)

    print("SCORE: " + str(score))
    print("STEP: " + str(step))

    for i in range(4):
        print(line_kugiri)
        print(line_blank)
        print(makeNumLine(board[i]))
        print(line_blank)
    
    print(line_kugiri)

def directionToRotation(direction):
    if(direction == "w"):
        rotation = 3
    elif(direction == "a"):
        rotation = 4
    elif(direction == "s"):
        rotation = 1
    elif(direction == "d"):
        rotation = 2
    
    return rotation

def quit():
    sys.exit()

def askDirection(board):
    # wasd to move
    inputStr = ""
    isInputOkey = False
    while(isInputOkey == False):
        inputStr = input("type your direction to move: ")
        if(inputStr in ["w","a","s","d"]):
            rotation = directionToRotation(inputStr)
            
            newBoard = moveBoard(board, rotation)
            if(board == newBoard):
                print("nothing will be changed!")
            else:
                isInputOkey = True
        elif(inputStr == ""):
            print("invalid input. try again.")
        elif(inputStr == "exit" or inputStr == "quit"):
            quit()
        else:
            print("invalid input. try again.")
    
    return rotation

def uniRotate(board):
    rBoard = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    # rotate board to clockwork direction
    for i in range(4):
        for j in range(4):
            rBoard[i][j] = board[3 - j][i]
    
    return rBoard

def rotateBoard(board, rotation):
    if(rotation == 0):
        return board

    for i in range(rotation):
        board = uniRotate(board)
    
    return board

def moveTile(board):
    isContinue = True

    while(isContinue):
        isContinue = False
        for i in range(4):
            for j in range(4):
                if(board[i][j] == 0):
                    continue
                
                if(j == 0):
                    # out of range回避用
                    continue

                if(board[i][j - 1] == 0):
                    isContinue = True
                    board[i][j - 1] = board[i][j]
                    board[i][j] = 0
                
                if(board[i][j] == board[i][j - 1]):
                    isContinue = True
                    board[i][j - 1] *= 2
                    board[i][j] = 0
                    addScore(board[i][j - 1])
    
    return board

def createTile(board, rate = 1.0):
    rate *= 100
    dice = random.randint(1,100)
    if(dice <= rate):
        pass
    else:
        return board

    tilePos = [0, 0]
    for i in range(2):
        tilePos[i] = random.randint(0, 3)
    
    while(board[tilePos[0]][tilePos[1]] != 0):
        for i in range(2):
            tilePos[i] = random.randint(0, 3)
    
    board[tilePos[0]][tilePos[1]] = random.randint(1, 2)
    return board

def moveBoard(board, rotation):
    # 天才的な仕組みをひらめいた
    # directionごとに動かす処理を書きなぐるのはつらいので
    # directionを相殺するようにboardを回転させて、同一の処理を行う

    # 動かしても何も変わらない方向はNG
    disrotation = 4 - rotation

    board = rotateBoard(board, rotation)
    board = moveTile(board)
    board = rotateBoard(board, disrotation)

    return board

def boardInit(initTileNum):
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    tilePositions = []
    for i in range(initTileNum):
        tilePositions.append([0, 0])
    
    while(allListEqual(tilePositions)):
        for i in range(initTileNum):
            for j in range(2):
                tilePositions[i][j] = random.randint(0, 3)

    for i in tilePositions:
        board[i[0]][i[1]] = random.randint(1, 2)

    return board

def checkEnd(board):
    if(0 in board):
        return False
    
    b1 = moveBoard(board, 1)
    b2 = moveBoard(board, 2)
    b3 = moveBoard(board, 3)
    b4 = moveBoard(board, 4)

    if(b1 == b2 == b3 == b4):
        return True
    else:
        return False

def main():
    global SCORE, STEP
    rate = 0.5
    getOS()
    consoleClear()

    gameInit()
    board = boardInit(initTileNum)

    isEnd = False

    while(isEnd == False):
        drow(board, SCORE, STEP)
        rotation = askDirection(board)
        STEP += 1
        board = moveBoard(board, rotation)
        board = createTile(board, rate)
        consoleClear()

        # for debug
        # board = DEBUG_BOARD

        isEnd = checkEnd(board)
        
    drow(board, SCORE, STEP)
    print("Game over!")

def gameInit():
    global SCORE, STEP
    SCORE = 0
    STEP = 0

def addScore(tileVal):
    global SCORE

    multi = 10
    SCORE += (tileVal ^ 2) * multi

main()
