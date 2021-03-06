import random
from math import exp
import time
from copy import deepcopy

def create_board(N):
    chess_board = {}
    temp = list(range(N))
    random.shuffle(temp)
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
    if N == 1:
        print("[1]")
        print("iter counter: 1")
        return
    if N == 2 or N==3:
        print("Failed")
        return

    threshold_of_iter = N * 200
    solution_found = False
    answer = create_board(N)
    cost_answer = cost(answer)
    counter = 0
    T = 4000
    d = 0.99
    while T > 0:
        counter += 1
        T *= d
        successor = deepcopy(answer)
        while True:
            index_1 = random.randrange(0, N - 1)
            index_2 = random.randrange(0, N - 1)
            if index_1 != index_2:
                break

        if counter == threshold_of_iter:
            print("again")
            return simulatedAnnealing(N)

        successor[index_1], successor[index_2] = successor[index_2], successor[index_1]
        delta = cost(successor) - cost_answer
        if delta < 0 or random.uniform(0, 1) < exp(-delta / T):
            answer = deepcopy(successor)
            cost_answer = cost(answer)

        if cost_answer == 0:
            solution_found = True
            print_chess_board(answer,N)
            print("iter counter: " + str(counter))
            return counter

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
    iter_counter = simulatedAnnealing(N)
    duration = time.time() - start
    print("SA for " + str(N) + " runtime in second:", duration)
    return duration,iter_counter
