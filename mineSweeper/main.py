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

def getNeighbor(board, y, x):
    height = len(board)
    width = len(board[0])

    # "nei" means Neighbor
    neis = []
    offsetsY = [-1, -1, -1, 0, 0, 1, 1, 1]
    offsetsX = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        nei = 0

        """
        try:
            nei = board[y + offsetsY[i]][x + offsetsX[i]]
        except IndexError:
            print()
            nei = 0
        """
        neiY = y + offsetsY[i]
        neiX = x + offsetsX[i]

        if not(0 <= neiY <= height - 1):
            nei = 0
            continue
        if not(0 <= neiX <= width - 1):
            nei = 0
            continue

        nei = board[neiY][neiX]
        
        neis.append(nei)
    
    return neis

def placeIndicater(board):
    height = len(board)
    width = len(board[0])

    for i in range(height):
        for j in range(width):
            if(board[i][j] == "b"):
                continue

            neis = getNeighbor(board, i, j)

            count = 0
            for k in neis:
                if(k == "b"):
                    count += 1
            
            board[i][j] = count

            """
            if(count == 0):
                board[i][j] = "b"
            else:
                board[i][j] = count  
            """ 
    
    return board

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
    

drow(placeIndicater(placeBomb(createBoard(6, 12), 70)))