# ps6pr5.py (Problem Set 6, Problem 5)
#
# 2-D Lists
#
# Computer Science 111
# 

import random

def create_grid(num_rows, num_cols):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = []
    
    for r in range(num_rows):
        row = [0] * num_cols     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line.
        input: grid is a 2-D list
    """
    num_rows = len(grid)
    for r in range(num_rows):
        if r == 0:
            print('[', end='')
        else:
            print(' ', end='')
        if r < num_rows - 1:
            print(str(grid[r]) + ',')
        else:
            print(str(grid[r]) + ']')

def random_grid(num_rows, num_cols):
    """ creates and returns a 2-D list with the specified dimensions
        in which each cell is assigned a random integer from 0-9.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = create_grid(num_rows, num_cols)

    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c] = random.choice(range(10))
            
    return grid


#function 1
def col_index_grid(num_rows, num_cols):
    """
    creates and returns a 2-D list with the specified dimensions in which each 
    cell has as its value the index of the column to which the cell belongs
    """
    grid = create_grid(num_rows, num_cols)
    for i in range(num_cols):
        for j in range(num_rows):
            grid [j][i] = i
            
    return grid


#function 2
def num_between(grid, n1, n2):
    """
    returns the number of values in grid that are between n1 and n2 – i.e., 
    greater than or equal to n1 and less than or equal to n2.
    """
    num = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] >= n1 and grid[i][j] <= n2:
                num += 1
                
    return num


#function 3
def copy(grid):
    """
    returns a deep copy of grid–a new, separate 2-D list that has the same 
dimensions and cell values as grid
    """
    new_grid = create_grid(len(grid), len(grid[0]))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid[i][j] = grid[i][j]
   
    return new_grid


#function 4
def double_with_cap(grid, cap):
   """
   the function should double the value of each element unless doing so would
cause the value of the element to be greater than cap. If doubling the element 
produces a value that is greater than cap, the element should be replaced with 
the value of cap instead.
   """
   for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] * 2 > cap:
                grid[i][j] = cap
            else:
                grid[i][j] = 2 * grid[i][j]
   

#function 5
def sum_evens_in_col(grid, colnum):
    """
    returns the sum of the even values in the column of grid whose index is colnum
    """
    sum = 0
    for i in range(len(grid)):
        if grid[i][colnum] % 2 == 0:
            sum += grid[i][colnum]
    
    return sum




                    
    

















