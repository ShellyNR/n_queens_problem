import random
from math import exp
import time
from copy import deepcopy

def create_board(N):
    chess_board = {}
    temp = list(range(N))
    random.shuffle(temp)  # shuffle to make sure it is random
    column = 0

    while len(temp) > 0:
        row = random.choice(temp)
        chess_board[column] = row
        temp.remove(row)
        column += 1
    del temp
    return chess_board

def threat_calculate(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    return (n - 1) * n / 2

def cost(chess_board):
    threat = 0
    m_chessboard = {}
    a_chessboard = {}

    for column in chess_board:
        temp_m = column - chess_board[column]
        temp_a = column + chess_board[column]
        if temp_m not in m_chessboard:
            m_chessboard[temp_m] = 1
        else:
            m_chessboard[temp_m] += 1
        if temp_a not in a_chessboard:
            a_chessboard[temp_a] = 1
        else:
            a_chessboard[temp_a] += 1

    for i in m_chessboard:
        threat += threat_calculate(m_chessboard[i])
    del m_chessboard

    for i in a_chessboard:
        threat += threat_calculate(a_chessboard[i])
    del a_chessboard

    return threat


def simulatedAnnealing(N):
    solution_found = False
    answer = create_board(N)
    cost_answer = cost(answer)
    counter = 0
    t = 4000
    sch = 0.99
    while t > 0:
        counter += 1
        t *= sch
        successor = deepcopy(answer)
        while True:
            index_1 = random.randrange(0, N - 1)
            index_2 = random.randrange(0, N - 1)
            if index_1 != index_2:
                break
        successor[index_1], successor[index_2] = successor[index_2], successor[index_1]  # swap two chosen queens
        delta = cost(successor) - cost_answer
        if delta < 0 or random.uniform(0, 1) < exp(-delta / t):
            answer = deepcopy(successor)
            cost_answer = cost(answer)
        if cost_answer == 0:
            solution_found = True
            print_chess_board(answer,N)
            print("iter counter: " + str(counter))
            break
    if solution_found is False:
        print("Failed")

def print_chess_board(board, N):
    showBoard = [[0 for j in range(N)] for i in range(N)]
    for column, row in board.items():
        showBoard[int(row)][int(column)] = 1
    for i in range(N):
        print(showBoard[i])

def SA(N):
    start = time.time()
    simulatedAnnealing(N)
    print("Runtime in second:", time.time() - start)
    exit()
