""" Python3 program to solve N Queen Problem using
backtracking """
N = 8
ind = N*2
its = 0
""" ld is an array where its indices indicate row-col+N-1 
(N-1) is for shifting the difference to store negative 
indices """
ld = [0] * ind

""" rd is an array where its indices indicate row+col 
and used to check whether a queen can be placed on 
right diagonal or not"""
rd = [0] * ind

"""column array where its indices indicates column and 
used to check whether a queen can be placed in that 
    row or not"""
cl = [0] * ind

""" A utility function to print solution """


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


""" A recursive utility function to solve N 
Queen problem """


def solveNQUtil(board, col, its):
#def solveNQUtil(board, col):
    """ base case: If all queens are placed
        then return True """

    if (col >= N):
        return True, its

    """ Consider this column and try placing
        this queen in all rows one by one """
    for i in range(N):

        """ Check if the queen can be placed on board[i][col] """
        """ A check if a queen can be placed on board[row][col].
        We just need to check ld[row-col+n-1] and rd[row+coln] 
        where ld and rd are for left and right diagonal respectively"""
        if ((ld[i - col + N - 1] != 1 and rd[i + col] != 1) and cl[i] != 1):

            """ Place this queen in board[i][col] """
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

            """ recur to place rest of the queens """
            sol, iterations = solveNQUtil(board, col + 1, its+1)
            its = iterations
            if (sol):
                return True, its

            """ If placing queen in board[i][col] 
            doesn't lead to a solution, 
            then remove queen from board[i][col] """
            board[i][col] = 0  # BACKTRACK
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0

            """ If the queen cannot be placed in
            any row in this column col then return False """
    return False, its


""" This function solves the N Queen problem using 
Backtracking. It mainly uses solveNQUtil() to 
solve the problem. It returns False if queens 
cannot be placed, otherwise, return True and 
prints placement of queens in the form of 1s. 
Please note that there may be more than one 
solutions, this function prints one of the 
feasible solutions."""


def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]
    sol, iterations = solveNQUtil(board, 0, its)
    if (sol == False):
        print("Solution does not exist")
        print ("iterations:", iterations)
        return False
    printSolution(board)
    print ("iterations:", iterations)
    return True


# Driver Code
solveNQ()

