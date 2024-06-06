import random as rd

# 一気に壊れる挙動が理解できない
# 調べる必要あり

def drow(board, mask, mes = ""):
    """
    <board>
    0 = empty
    1 = bomb

    board = [
        [0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1]
    ]


    <mask>
    0 = unmasked
    1 = masked

    mask = [
        [0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1]
    ]
    """