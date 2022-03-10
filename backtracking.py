def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, its):
    # base case: If all queens are placed
    # then return true
    if col >= N:
        return True, its

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):
        its += 1
        if isSafe(board, i, col):

            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            sol, iterations = solveNQUtil(board, col + 1, its)
            its = iterations
            if sol == True:
                return True, its
            board[i][col] = 0
    return False, its


def solveNQ(N):
    its = 0
    board = [[0 for _ in range(N)] for _ in range(N)]
    sol, iterations = solveNQUtil(board, 0, its)
    if (sol == False):
        # if (solveNQUtil(board, 0) == False):
        print("Solution does not exist")
        print("iterations:", iterations)
        return False
    printSolution(board)
    print("iterations:", iterations)
    return True
