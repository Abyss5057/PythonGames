import random as rd

# 一気に壊れる挙動が理解できない
# 調べる必要あり

def createBoard(height, width):
    board = []
    for i in range(height):
        board.append([0] * width)
    
    return board

def placeBomb(board, num):
    height = len(board)
    width = len(board[0])

    if(height * width < num):
        print("The number of bomb is larger than board!")
        return

    bombPos = []

    for i in range(num):
        x = rd.randint(0, width - 1)
        y = rd.randint(0, height - 1)

        while([x, y] in bombPos):
            x = rd.randint(0, width - 1)
            y = rd.randint(0, height - 1)
        
        bombPos.append([x, y])
        board[y][x] = "b"
    
    return board

def placeIndicater(board):
    pass

def drow(board, mask = [], mes = ""):
    isHideZero = True

    height = len(board)
    width = len(board[0])

    for i in range(height):
        line = ""
        for j in range(width):
            line += str(board[i][j])
        
        if(isHideZero):
            line = line.replace("0", " ")
        
        print(line)
    

drow(placeBomb(createBoard(4, 8), 5))