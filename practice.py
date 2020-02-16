#!/usr/bin/env python3
import numpy as np
from tqdm import tqdm


# (max # of slices) , (# of pizza types)
# (pizza 0 slices), (pizza 1 slices), ...bin

max_slices = 10000
remaining_slices = max_slices
pizza_types = []
slice_remaining = max_slices

# track pizza combinations, 0/1 pizza box
# pizza_box = [[] for pizza in pizza_types]

for pizza in pizza_types[::-1]:
    #check pizza > available slices
    if pizza > slice_remaining:
        break
    slice_remaining = max_slices - pizza
    
    

# Returns the maximum value that can be put in a pizza_box of 
# capacity W 

# A Dynamic Programming based Python Program for 0-1 pizza_box problem 
# Returns the pizza_box
def pizza_box(capacity, pizza_types): 
    n = len(pizza_types)
    K = np.zeros((n+1, capacity+1), dtype=int)

    # Build table K[][] in bottom up manner 
    for i in tqdm(range(n+1)):


        # only parallelize this loop
        for w in tqdm(range(capacity+1)): 
            if i==0 or w==0: 
                # K[i, :w] = 0
                K[i][w] = 0
            elif pizza_types[i-1] <= w: 
                # K[i, :w] = max(pizza_types[i-1] + K[i-1, :w-pizza_types[i-1]],  K[i-1, :w]) 
                K[i][w] = max(pizza_types[i-1] + K[i-1][w-pizza_types[i-1]],  K[i-1][w]) 
            else: 
                # K[i, :w] = K[i-1, :w]
                K[i][w] = K[i-1][w] 
  
    return K



def get_output_from_pizza_box(capactiy, pizza_types, pizza_box):
    types_to_order = []
    w = capactiy
    n = len(pizza_types)

    res = pizza_box[n][capactiy]
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        if res == pizza_box[i - 1][capactiy]: 
            continue
        else: 
  
            # This item is included. 
            types_to_order.append(i - 1)
              
            # Since this weight is included 
            # its value is deducted 
            res = res - pizza_types[i - 1] 
            w = w - pizza_types[i - 1] 

    types_to_order = sorted(types_to_order)
    return len(types_to_order), types_to_order

def get_input(file_name):
    capacity = None
    pizza_type = None
    with open(file_name) as descriptor:
        print("reading file")
        line = descriptor.readline().split(" ")
        capacity = int(line[0])
        pizza_types = descriptor.readline().split(" ")
        print("got types")
        pizza_types = [int(item) for item in pizza_types]
        print("converted types")
    return capacity, pizza_types

def write_output(number_to_order, types_to_order, path):
    with open(path, "w") as output:
        output.write("{}\n".format(number_to_order))
        output.write(' '.join(str(p) for p in types_to_order))
    


def main():
    capacity, pizza_types = get_input("d_quite_big.in")
    box = pizza_box(capacity, pizza_types)
    number_of_pizza_types, types_to_order = get_output_from_pizza_box(
        capacity, pizza_types, box
    )
    write_output(number_of_pizza_types, types_to_order, "d_quite_big.out_actual")

if __name__ == "__main__":
    main()
