# https://www.hackerrank.com/challenges/candies/problem?isFullScreen=true

import random


def min_num_of_candies(arr):
    def adjust_candies_to_prev(idx, arr, candies):
        current_score = arr[idx]

        prev_idx = idx - 1
        prev_score = arr[prev_idx]

        current_idx_candies = candies[idx]
        prev_idx_candies = candies[prev_idx]

        if current_score > prev_score \
                and current_idx_candies <= prev_idx_candies:
            candies[idx] = candies[prev_idx] + 1

        elif current_score < prev_score \
                and current_idx_candies >= prev_idx_candies:
            candies[prev_idx] = candies[idx] + 1

    candies = [1 for _ in arr]

    # first pass, "left to right"
    for idx in range(1, len(arr)):
        adjust_candies_to_prev(idx, arr, candies)

    reversed_arr = list(reversed(arr))
    candies = list(reversed(candies))

    # second pass, "right to left"
    for idx in range(1, len(arr)):
        adjust_candies_to_prev(idx, reversed_arr, candies)

    # print(candies)
    return sum(candies)


arr1 = [4, 6, 4, 5, 6, 2]  # [1, 2, 1, 2, 3, 1] 10
arr2 = [1, 2, 2]  # [1, 2, 1] 4
arr3 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]  # 19
arr4 = [2, 4, 3, 5, 2, 6, 4, 5]  # 12

arr5 = [8, 7, 4, 3]  # 10
arr6 = [3, 4, 7, 8]  # 10

rand_arr = [random.randint(0, 9) for _ in range(random.randint(2, 10))]

print(min_num_of_candies(arr1))
print(min_num_of_candies(arr2))
print(min_num_of_candies(arr3))
print(min_num_of_candies(arr4))
print(min_num_of_candies(arr5))
print(min_num_of_candies(arr6))

print(rand_arr)
print(min_num_of_candies(rand_arr))