#!/usr/bin/python3

""" contains n queens problem solution """


import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    N = int(sys.argv[1])

except ValueError:
    print("N must be a number")
    exit(1)


if N < 4:
    print("N must be at least 4")
    exit(1)

def verify_solution(sol, N):
    """ Takes a list of indecies, and verify it """

    if len(sol) != N:
        return False
    
    for i in range(len(sol)):
        row_1 = sol[i][0]
        col_1 = sol[i][1]

        for j in range(i + 1, len(sol)):
            row_2 = sol[j][0]
            col_2 = sol[j][1]

            if row_1 == row_2 or col_1 == col_2:
                return False
            if abs(row_1 - row_2) == abs(col_1 - col_2):
                return False

    return True


def rec_sol(size, row=0, col=0, current_sol=[]):
    if row >= size:
        if verify_solution(current_sol, size):
            print(current_sol)
        return

    if col == size - 1:
        new_col = 0
        new_row = row + 1
    else:
        new_col = col + 1
        new_row = row
    rec_sol(size, new_row, new_col, current_sol)
    current_sol.append([row, col])
    rec_sol(size, row + 1, 0, current_sol)
    current_sol.pop()


rec_sol(N)
