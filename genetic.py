import random
import time

def print_board(board):
    for row in board:
        print(row)

def create_final_board(nq, chrom_out):
    board = []
    for x in range(nq):
        board.append([0] * nq)
    for i in range(nq):
        board[nq - chrom_out[i]][i] = 1
    return board

def init_population(nq):  # making random chromosomes
    return [random.randint(1, nq) for _ in range(nq)]

def fitness(maxFitness,chromosome):
    horizontal_collisions = sum([chromosome.count(queen) - 1 for queen in chromosome]) / 2

    n = len(chromosome)
    left_diagonal = [0] * 2 * n
    right_diagonal = [0] * 2 * n
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2 * n - 1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1
        diagonal_collisions += counter / (n - abs(i - n + 1))

    return int(maxFitness - (horizontal_collisions + diagonal_collisions))

def probability(maxFitness,chromosome, fitness):
    return fitness(maxFitness,chromosome) / maxFitness

def parents_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    exit() # in error case, should not happened

def reproduce(x, y):  # doing cross_over between two chromosomes
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def mutate(x):  # randomly changing the value of a random index of a chromosome
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def change_population(maxFitness,population, fitness,mut_prob):
    new_population = []
    probabilities = [probability(maxFitness,n, fitness) for n in population]
    for i in range(len(population)):
        x = parents_pick(population, probabilities)
        y = parents_pick(population, probabilities)
        child = reproduce(x, y)
        if random.random() < mut_prob:
            child = mutate(child)
        new_population.append(child)
        if fitness(maxFitness,child) == maxFitness: break
    return new_population

def geneticAlgo(N,pop_size,mut_prob):
    threshold_of_iter = N * 200
    nq = N
    maxFitness = (nq * (nq - 1)) / 2
    population = [init_population(nq) for _ in range(pop_size)]
    counter = 0

    while not maxFitness in [fitness(maxFitness,chrom) for chrom in population]:
        population = change_population(maxFitness,population, fitness,mut_prob)
        counter += 1
        if counter == threshold_of_iter:
            print("again")
            return geneticAlgo(N, pop_size,mut_prob)
            # print("Failed")
            # return 0


    for chrom in population:
        if fitness(maxFitness,chrom) == maxFitness:
            # chrom_out = chrom
            # board = create_final_board(nq, chrom_out)
            # print_board(board)
            # print("iter counter {}".format(counter))

            return counter
            # print("Success")
            # return 1

def GA(N,pop_size,mut_prob):
    if N == 2 or N == 3:
        # print("Failed")
        return 0, 0 # failed
    start = time.time()
    iter_counter = geneticAlgo(N,pop_size,mut_prob)
    duration = time.time() - start
    print("pop size: " +str(pop_size) + " mut prob: " +  str(mut_prob) +" N is: " + str(N) + " Runtime in second: " + str(duration)+ " iter: "+ str(iter_counter))
    return duration,iter_counter
    # return geneticAlgo(N,pop_size,mut_prob)
