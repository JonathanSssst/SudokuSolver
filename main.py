sudoku = [
    [0, 0, 0, 9, 0, 0, 0, 7, 1],
    [9, 0, 0, 0, 0, 3, 0, 5, 0],
    [0, 2, 5, 0, 4, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 1, 6, 0],
    [0, 4, 0, 8, 0, 1, 0, 0, 0],
    [0, 0, 6, 5, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 9, 2, 6, 0, 0],
    [2, 9, 8, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 9],
]


def print_sudoku(sudoku):
    """print sudoku"""
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')
        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')
            print(sudoku[i][j], end=' ')
        print()


def is_valid(sudoku, row, col, num):
    """check if the number is valid in the position"""
    # check row
    for x in range(9):
        if sudoku[row][x] == num:
            return False

    # check column
    for x in range(9):
        if sudoku[x][col] == num:
            return False

    # check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[i + start_row][j + start_col] == num:
                return False

    return True


def solve(sudoku):
    """solve sudoku"""

    # find empty cell
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                # try number 1-9
                for num in range(1, 10):
                    if is_valid(sudoku, row, col, num):
                        # fill the number
                        sudoku[row][col] = num

                        # recursive solve the rest
                        if solve(sudoku):
                            return True

                        # if not solved, backtrack
                        sudoku[row][col] = 0

                # try all numbers, none is valid, return False
                return False

    # if no empty cell, the sudoku is solved
    return True

if solve(sudoku):
    print_sudoku(sudoku)
else:
    print('Failed to solve the sudoku')

