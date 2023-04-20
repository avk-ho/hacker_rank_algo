# https://www.hackerrank.com/challenges/angry-children/problem?isFullScreen=true

import random

def max_min(k, arr):
    if k == 1:
        return [arr[0]], 0

    sorted_arr = sorted(arr)
    min_unfairness_arr = []

    i, j = 0, k - 1
    min_unfairness = None
    while j < len(sorted_arr):
        unfairness = sorted_arr[j] - sorted_arr[i]

        if min_unfairness is None or min_unfairness > unfairness:
            min_unfairness = unfairness
            min_unfairness_arr = sorted_arr[i:j+1]

        i += 1
        j += 1

    return min_unfairness_arr, min_unfairness


test1 = [2, [1, 4, 7, 2]]  # 1
test2 = [3, [10, 100, 300, 200, 1000, 20, 30]]  # 20
test3 = [4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]]  # 3
test4 = [2, [1, 2, 1, 2, 1]]  # 0

rand_k = random.randint(2, 5)
rand_arr = [random.randint(0, 100) for _ in range(random.randint(rand_k, 10))]
rand_test = [rand_k, rand_arr]

print(max_min(*test1))
print(max_min(*test2))
print(max_min(*test3))
print(max_min(*test4))
print(*rand_test)
print(max_min(*rand_test))