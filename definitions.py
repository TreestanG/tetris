
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

shape_colors = {
    "I": CYAN,
    "O": YELLOW,
    "T": MAGENTA,
    "L": ORANGE,
    "J": BLUE,
    "S": GREEN,
    "Z": RED
}

block_size = 30
shape_size = 4

tetris_grid = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

shapes = {
    "I":[[1,2,3,4], [3,7,11,15], [9,10,11,12], [2,6,10,14]],
    "O":[[2,3,6,7], [2,3,6,7], [2,3,6,7], [2,3,6,7]],
    "T":[[2,5,6,7], [2,6,7,10], [5,6,7,10], [2,5,6,10]],
    "L":[[2,6,10,11], [5,6,7,9], [1,2,6,10], [3,5,6,7]],
    "J":[[2,6,9,10], [1,5,6,7], [2,3,6,10], [5,6,7,11]],
    "S":[[2,3,5,6], [2,6,7,11], [2,3,5,6], [2,6,7,11]],
    "Z":[[1,2,6,7], [3,6,7,10], [1,2,6,7], [3,6,7,10]]
}

shape_dimensions = {
    "I":[4,1],
    "O":[2,2],
    "T":[3,2],
    "L":[3,2],
    "J":[3,2],
    "S":[3,2],
    "Z":[3,2]
}

dimensions = {
    "I":[[0, -2, 0, 1], [2, 1, 2, 0]], # Distance away from border
    "O":[[-1, -1, -1, -1], [1,1,1,1]],
    "T":[[0, -1, 0, 0], [1, 1, 1, 0]],
    "L":[[-1, 0, 0, 0], [1, 1, 0, 1]],
    "J":[[0, 0, -1, 0], [0, 1, 1, 0]],
    "S":[[0, -1, 0, 1], [1, 1, 1, 1]],
    "Z":[[0, -1, 0, 1], [1, 1, 1, 0]]
}
"""
"""
bricks = {
    0:'empty',
    1:CYAN,
    2:YELLOW,
    3:MAGENTA,
    4:ORANGE,
    5:BLUE,
    6:GREEN,
    7:RED,
}

tetris_matrix = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [2,2,0,0,0,0,0,0,0,0],
    [2,2,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0,0,0], # 20 rows    
]