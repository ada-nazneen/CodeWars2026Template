# Student reference: https://docs.google.com/document/d/1Sb6iyO5pepmMdJTFuHcvDrsBrWMk5iPDWfXv1cbbO-U/preview?usp=sharing

import sudokuLibBasic as sl

def sudokuCoordinates(coords):
    return [int(coords[0]), int(coords[2])]

def is_valid_move(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return False
        if sudoku[i][col] == num:
            return False

    # start_row = (row // 3) * 3
    # start_col = (col // 3) * 3
    # for i in range(3):
    #     for j in range(3):
    #         if sudoku[start_row + i][start_col + j] == num:
    #             return False
    # return True
    indextostart=[0,0,0,3,3,3,6,6,6]
    start_col = indextostart[col]
    start_row = indextostart[row]
    for i in range(3):
        for j in range(3):
            if sudoku[start_row][start_col] == num:
                return False
    return True

sudoku = sl.sudokus[0]

while True:
    sl.display_sudoku(sudoku)
    pizza=int(input("What number would yoou like to place"))
    position=sudokuCoordinates(input("x,y"))
    if is_valid_move(sudoku, position[0],position[1],pizza):
        sudoku[position[0]][position[1]]=pizza
    else:
        print("error")