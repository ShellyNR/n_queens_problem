# Python3 program to solve N Queen
# Problem using backtracking
import time
its = 0

def printSolution(board,N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens
def isSafe(board,N, row, col):
    # Check this row on left side
    count = 0
    for i in range(col):
        #count += 1
        if board[row][i] == 1:
            return False, count

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        #count += 1
        if board[i][j] == 1:
            return False, count

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        #count += 1
        if board[i][j] == 1:
            return False, count

    return True, count


def solveNQUtil(board,N, col, its):
    # base case: If all queens are placed
    # then return true
    if col >= N:
        return True, its

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):
        its += 1
        legal , it = isSafe(board,N, i, col)
        its +=it
        if legal:

            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            sol, iterations = solveNQUtil(board,N, col + 1, its)
            its = iterations
            if sol == True:
                return True, its

            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in
    # this column col then return false
    return False, its


# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns false if queens
# cannot be placed, otherwise return true and
# placement of queens in the form of 1s.
# note that there may be more than one
# solutions, this function prints one of the
# feasible solutions.
def solveNQ(n):
    N=n
    board = [[0 for _ in range(N)] for _ in range(N)]
    start = time.time()
    sol, iterations = solveNQUtil(board,N, 0, its)
    end = time.time()
    elapsed = end - start
    if (sol == False):
        # if (solveNQUtil(board, 0) == False):
        print("Solution does not exist")
        print("iterations:", iterations)
        return elapsed, 0
    printSolution(board,N)
    print("iterations:", iterations)
    return elapsed, iterations

def board_solveNQ(n):
    N=n
    board = [[0 for _ in range(N)] for _ in range(N)]
    start = time.time()
    sol, iterations = solveNQUtil(board,N, 0, its)
    end = time.time()
    elapsed = end - start
    if (sol == False):
        # if (solveNQUtil(board, 0) == False):
        print("Solution does not exist")
        return 0
    printSolution(board,N)


def backtracking(n):
    board_solveNQ(n)
# Driver Code
#solveNQ(8)

# This code is contributed by Divyanshu Mehta
