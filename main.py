import backtracking
import branch_and_bound
import hillclimbing
import simulated_annealing

if __name__ == '__main__':
    N = int(input("Enter size of N: "))
    print("\nChoose from menu: \n1.backtracking\n2.branch and bound\n3.hillclimbing\n4.simulated annealing\n")
    algoNumber = input("Enter algo number: ")
#     N = 8
#     algoNumber = 1
#     sa.simulated_annealing(N)
    algoDic = {
        1 : backtracking.backtracking(N),
        2 : branch_and_bound.BNB(N),
#         3 : hillclimbing.hillclimbing(N),
        4 : simulated_annealing.SA(N),

    }[algoNumber]
