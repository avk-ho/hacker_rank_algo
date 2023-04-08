# https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

def diagonal_difference(matrix):
    n = len(matrix)

    sum1 = 0 # top left bottom right
    sum2 = 0 # top right bottom left

    i = 0
    j = n - 1
    while i < n:
        sum1 += matrix[i][i]
        sum2 += matrix[i][j]

        i += 1
        j -= 1

    return abs(sum1 - sum2)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
    ]

matrix2 = [
    [8, 2],
    [5, 7]
]

print(diagonal_difference(matrix))
print(diagonal_difference(matrix2))