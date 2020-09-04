import numpy as np

""" Analogous approach of recursive_sudy.py. The only difference is that one can define the sudoku to be solved 
    interactively on the terminal"""

print("Write each element of the sudoku (write 0 in case of an empty cell). \nProceed by row.")
raw_matrix = []
for i in range(81):
    n = int(input("Write the next element:"))
    raw_matrix.append(n)
sudoku = [raw_matrix[k:k + 9] for k in range(0, len(raw_matrix), 9)]


def possible(x, y, n):
    """ Check if the digit n could fill the square of coordinate (x,y).
           Args_1:
             x, y (int): coordinates of the cell.
           Args_2:
             n (int): candidate to fill the square.
    """
    global sudoku
    for j in range(0, 9):
        if sudoku[x][j] == n:
            return False
    for i in range(0, 9):
        if sudoku[i][y] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[x0 + i][y0 + j] == n:
                return False
    return True


def solve():
    """ Solve the sudoku using the function "possible".
        Recursion is used as a better way to implement backtracking.
        Returns all the solutions.
    """
    global sudoku
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        sudoku[x][y] = n
                        solve()
                        sudoku[x][y] = 0
                return
    print(np.array(sudoku))
    input("More?")


solve()

