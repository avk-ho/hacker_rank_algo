# https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true

def circular_array_rotation(arr, nb_rotation, queries):
    rotated_arr = [None for _ in arr]
    for idx in range(len(arr)):
        new_idx = (idx + nb_rotation) % len(arr)
        rotated_arr[new_idx] = arr[idx]

    result = []

    for query in queries:
        result.append(rotated_arr[query])

    return result


# [arr, nb_rotation, queries]
test1 = [[3, 4, 5], 2, [1, 2]]
test2 = [[1, 2, 3], 2, [0, 1, 2]]

print(circular_array_rotation(*test1))
print(circular_array_rotation(*test2))