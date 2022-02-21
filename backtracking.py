its = 0

def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(N, board, col, its):
    if col >= N:
        return True, its

    for i in range(N):
        its += 1
        if isSafe(board, i, col):
            board[i][col] = 1
            sol, iterations = solveNQUtil(board, col + 1, its)
            its = iterations
            if sol == True:
                return True, its

            board[i][col] = 0

    return False, its

def backtracking(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    sol, iterations = solveNQUtil(board, 0, its)
    if (sol == False):
        # if (solveNQUtil(N, board, 0) == False):
        print("Solution does not exist")
        print("iterations:", iterations)
        exit()
    printSolution(board, N)
    print("iterations:", iterations)
    exit()
