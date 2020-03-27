import numpy as np

def init_unassigned(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                grid[i][j] = 10
    return grid



# returns false if no double has been found
def check_square_doubles(grid,x,y):
    array_true = np.full((9,), False)
    for i in range(3):
        for j in range(3):
            if array_true[grid[x+i,y+j]]:
                return True
            array_true[grid[x+i,y+j]] = True

    return False

def check_row_doubles(grid,row):
    array_true = np.full((9,), False)
    for i in range(9):
        if array_true[grid[row,i]]:
            return True
        array_true[grid[row,i]] = True
    return False




def valid_grid(grid):

    found_double = False

    for i in range(3):
        for j in range(3):
            if check_square_doubles(grid, i * 3, j*3):
                return False

    for row in range(9):
        if check_row_doubles(grid, row):
            return False













def naive_solver(grid):
    
    return valid_grid(grid)

grid = np.full((9, 9), 0)
grid = grid.copy()

print(naive_solver(np.full((9, 9), 0)))


