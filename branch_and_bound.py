
def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def solveNQUtil(N, board, col, its):
    if (col >= N):
        return True, its

    for i in range(N):
        if ((ld[i - col + N - 1] != 1 and rd[i + col] != 1) and cl[i] != 1):

            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

            sol, iterations = solveNQUtil(N, board, col + 1, its+1)
            its = iterations
            if (sol):
                return True, its

            board[i][col] = 0  # BACKTRACK
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
    return False, its

def BNB(N):
    ind = N * 2
    global its
    global ld
    global rd
    global cl
    its = 0
    ld = [0] * ind
    rd = [0] * ind
    cl = [0] * ind

    board = [[0 for _ in range(N)] for _ in range(N)]
    sol, iterations = solveNQUtil(N, board, 0, its)
    if (sol == False):
        print("Solution does not exist")
        print ("iterations:", iterations)
        exit()
    printSolution(board, N)
    print ("iterations:", iterations)
    exit()
