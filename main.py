import backtracking
import branch_and_bound
import hill_climbing
import simulated_annealing
import genetic

def execute(algoNumber, N):
    if algoNumber == 1:
        backtracking.backtracking(N)
    elif algoNumber == 2:
        branch_and_bound.BNB(N)
    elif algoNumber == 3:
        hill_climbing.HC(N)
    elif algoNumber == 4:
        simulated_annealing.SA(N)
    elif algoNumber == 5:
        genetic.GA(N,100,0.3)
    else:
        print("wrong Number")

if __name__ == '__main__':
    N = int(input("Enter size of N: "))
    print("\nChoose from menu: \n1.Backtracking Algorithm\n2.Branch And Bound\n3.Hill climbing\n4.Simulated Annealing\n5.Genetic Algorithm")
    algoNumber = int(input("Enter algo number: "))
    execute(algoNumber,N)
