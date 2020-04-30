import numpy as np
from math import floor
import time

# returns false if no double has been found
def check_square_doubles(grid,x, y):
    array_true = np.full((9,), False)
    for i in range(9):
        x_in_square = floor(i/3)
        y_in_square = i%3
        #print(i)
        #print("grid is: ",grid)

        element = grid[x+x_in_square][y+y_in_square] 
        element -= 1

       
        if array_true[element]:
            return True
        array_true[element] = True

    return False

def check_row_doubles(grid,row):
    array_true = np.full((9,), False)
    for i in range(9):
        if array_true[grid[row,i]]:
            return True
        array_true[grid[row,i]] = True
    return False



# checks whether current grid has no constraints
def valid_grid(grid):
    found_double = False

    print(grid)

    for i in range(3):
        for j in range(3):
            if check_square_doubles(grid, i * 3, j*3):
                return False

    for row in range(9):
        if check_row_doubles(grid, row):
            return False

#def valid_grid(grid,array_unit_cells,idx)

def fill_grid_naive(grid):
    last_filled = False
    array_unit_cells = find_unitialised_cells(grid) # these are the variables in CSP, domain is from 1-9
    
    while not last_filled:
        grid = fill_grid_once(grid,array_unit_cells) 
        if valid_grid(grid):
            return grid
        last_filled = is_last_fill(grid,array_unit_cells) 

    print("could not be filled")
    return False


def fill_grid_backtracking(grid):
    last_filled = False
    array_unit_cells = find_unitialised_cells(grid) # these are the variables in CSP, domain is from 1-9
    index = 0
    
    end = fill_next(grid,index, array_unit_cells)

    if not end:
        print("couldn't fill this sudoku")

    return grid

    
 


def fill_next(grid,idx,array_unit_cells):

    x_and_y_grid = array_unit_cells[idx] 

    x = x_and_y_grid[0]
    y = x_and_y_grid[1]

    current_element = grid[x,y] 


    while(grid[x,y] < 9):
        grid[x,y] += 1

        print("index: {", x,y,"}")
        if valid_added_element(grid,x,y):

            if idx == len(array_unit_cells) -1 :
                return True
            if fill_next(grid,idx+1, array_unit_cells):
                return True
    grid[x,y] = 0
    return False



def valid_added_element(grid,x,y):

    print(grid) 
    #check square

    x_square = floor(x / 3)
    y_square = floor(y / 3)

    x_square *= 3
    y_square *= 3
    array_true = np.full((9,), False)

    for i in range(3):
        for j in range(3):

            element = grid[i+x_square,j +y_square] - 1
            if element == -1:
                continue

            if array_true[element]:
                return False
            else:
                array_true[element] = True

    print("after square")
    #check row
    array_true = np.full((9,), False)

    for i in range(9):
        element = grid[i,y] - 1
        if element == -1:
            continue

        if array_true[element]:
            return False
        else:
            array_true[element] = True
    print("after column")
    #check row
    array_true = np.full((9,), False)

    for i in range(9):
        element = grid[x,i] -  1
        if element == -1:
            continue

        if array_true[element]:
            return False
        else:
            array_true[element] = True

    print("after row")

    return True


def is_last_fill(grid,unit_cells):
    return grid[0][0] == -1
         



def find_unitialised_cells(grid):
    lst = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                lst.append([i, j])
                #grid[i][j] = 1


    return lst



def fill_grid_once(grid, unit_cells):

    current = 0
    while current < len(unit_cells):
        x_coordinate = unit_cells[current][0]
        y_coordinate = unit_cells[current][1]


        if grid[x_coordinate][y_coordinate] in range(9): # even 0 will be included
            grid[x_coordinate][y_coordinate] += 1
            return grid
        elif current == len(unit_cells):
            grid[0][0] = -1 # First unit element false -> last element
            return grid
        else:
            grid[x_coordinate][y_coordinate] = 1

        current += 1



def naive_solver(grid):
    
    return fill_grid_naive(grid)


def backtracking_solver(grid):

    return fill_grid_backtracking(grid)

grid = np.array([[2,9,0,0,0,0,0,7,0],
    [3,0,6,0,0,8,4,0,0],
    [8,0,0,0,4,0,0,0,2],
    [0,2,0,0,3,1,0,0,7],
    [0,0,0,0,8,0,0,0,0],
    [1,0,0,9,5,0,0,6,0],
    [7,0,0,0,9,0,0,0,1],
    [0,0,1,2,0,0,3,0,6],
    [0,3,0,0,0,0,0,5,9]])

#grid = np.full((9, 9), 0)
start = time.time()
print(backtracking_solver(grid))
end = time.time()
print(end - start)
