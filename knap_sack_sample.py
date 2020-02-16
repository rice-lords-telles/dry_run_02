import numpy as np


def main():
    

    values = np.array([3,4,3,5,8,10])
    weights = np.array([2,5,6,8])
    items = len(weights)
    capacity = 17

    memo = dict()
    for size in range(0, capacity+1, 1):
        memo[(-1, size)] = ([], 0)

    for item in range(items):
        for size in range(0, capacity+1, 1):
            #if the object doesn't fit in the knapsack
            if weights[item] > size:
                memo[item, size] = memo[item-1, size]
            else:
                #if the obj fits, we check what can best fit in the residual space
                previous_row, previous_row_value = memo[item-1, size-weights[item]]
                if memo[item-1, size][1] > values[item] + previous_row_value:
                    memo[item, size] = memo[item-1, size]
                else:
                    memo[item, size] = (previous_row + [item], previous_row_value + values[item])

    best_set, score = memo[items-1, capacity]
    print("The best set %s weights %i and values %i" % (best_set, np.sum(weights[best_set]), score))

if __name__ == '__main__':
    main()