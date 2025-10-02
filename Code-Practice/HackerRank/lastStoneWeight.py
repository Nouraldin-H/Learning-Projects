#!/bin/python3
# goals:
# - sort array by lowest to highest [2, 7, 8, 9] example
# - iterate over array from last to first element i.e. 9 is last element
# - weights are equal? remove both from array
# - weights not equal? subtract highest element with lowest element
# - no elements in array? return 0

# function expected to return INTEGER
# function accepts INTEGER_ARRAY weights as parameter

def lastStoneWeight(weights):
    while len(weights) > 1:
        weights.sort()
        heavy1 = weights.pop()
        heavy2 = weights.pop()
        
        if heavy1 >= heavy2:
            weights.append(heavy1 - heavy2)
        # for i in reversed(weights):
        #     if i == i + 1:
        #         weights.remove(i)
        #         weights.remove(i + 1)
        #     elif i > i + 1:
        #         weights.remove(i + 1)
        #     elif i < i + 1:
        #         weights.remove(i)

        return weights[0]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    weights_count = int(input().strip())

    weights = []

    for _ in range(weights_count):
        weights_item = int(input().strip())
        weights.append(weights_item)

    result = lastStoneWeight(weights)

    fptr.write(str(result) + '\n')

    fptr.close()