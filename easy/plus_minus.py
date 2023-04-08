# https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

import random

def plus_minus(arr):
    n = len(arr)

    decimal_places = 6

    num_pos = 0
    num_neg = 0
    num_zero = 0

    for i in range(n):
        if arr[i] > 0:
            num_pos += 1
        elif arr[i] < 0:
            num_neg += 1
        else:
            num_zero += 1

    result = [round(num_pos / n, decimal_places), 
              round(num_neg / n, decimal_places),
              round(num_zero / n, decimal_places)
              ]
    
    for elem in result:
        print(elem)


# arr = [1, 1, 0, -1, -1]
# arr2 = [-4, 3, -9, 0, 4, 1]
# plus_minus(arr)
# plus_minus(arr2)

arr = [random.randint(-1, 1) for _ in range(random.randint(1, 10))]
print(arr, len(arr))
plus_minus(arr)