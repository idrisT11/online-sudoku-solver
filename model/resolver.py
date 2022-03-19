

from random import randint
import numpy as np


def get_first_empty_cell(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j

    return -1, -1

def impossible(sudoku):
    for k in range(9):
        values = []
        for i in range(3):
            for j in range(3):
                x = (k//3)*3 + i
                y = (k%3)*3 + j

                val = sudoku[x][y]
                if val == 0: 
                    continue

                if val in values:
                    return True
                else:
                    values.append(val)

    for i in range(9):
        values_x = []
        values_y = []

        for j in range(9):
            val_x = sudoku[i][j]
            val_y = sudoku[j][i]

            if val_x != 0:
                if val_x in values_x:
                    return True
                else:
                    values_x.append(val_x)

            if val_y != 0:
                if val_y in values_y:
                    return True
                else:
                    values_y.append(val_y)
    
    return False


def resolved(sudoku):

    x, y = get_first_empty_cell(sudoku)

    if x != -1: return False

    return not impossible(sudoku)


def resolve(sudoku):
    if impossible(sudoku):
        return False

    if resolved(sudoku):
        return True

    else:
        x, y = get_first_empty_cell(sudoku)
        if x == -1: return True

        for i in range(9):
            j = i + 1
            sudoku[x][y] = j
            gut = resolve(sudoku)

            if randint(0, 200) == 1:
                print(sudoku)

            if gut:
                return True

        sudoku[x][y] = 0
        #print(sudoku)
        #input()
        return False


tab = np.array([
    [8 , 0, 0, 0, 1, 0, 0, 0, 9],
    [0 , 5, 0, 8, 0, 7, 0, 1, 0],
    [0 , 0, 4, 0, 9, 0, 7, 0, 0],
    [0 , 6, 0, 7, 0, 1, 0, 2, 0],
    [5 , 0, 8, 0, 6, 0, 1, 0, 7],
    [0 , 1, 0, 5, 0, 2, 0, 9, 0],
    [0 , 0, 7, 0, 4, 0, 6, 0, 0],
    [0 , 8, 0, 3, 0, 9, 0, 4, 0],
    [3 , 0, 0, 0, 5, 0, 0, 0, 8]
])

gut = resolve(tab)
print(gut)
print(tab)

