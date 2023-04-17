# https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem?isFullScreen=true

import random


def max_num_of_connected_cells_in_matrix(matrix):
    def find_all_connected_cells(row, col, visited_matrix, new_region):
        if matrix[row][col] == 0:
            return

        if visited_matrix[row][col] == True:
            return

        visited_matrix[row][col] = True
        new_region.append((row, col))
        above_row, below_row = row - 1, row + 1
        left_col, right_col = col - 1, col + 1

        if above_row >= 0:
            # above
            find_all_connected_cells(
                above_row, col, visited_matrix, new_region)

            # diagonal above left
            if left_col >= 0:
                find_all_connected_cells(
                    above_row, left_col, visited_matrix, new_region)

            # diagonal above right
            if right_col < len(visited_matrix[0]):
                find_all_connected_cells(
                    above_row, right_col, visited_matrix, new_region)

        if below_row < len(visited_matrix):
            # below
            find_all_connected_cells(
                below_row, col, visited_matrix, new_region)

            # diagonal below left
            if left_col >= 0:
                find_all_connected_cells(
                    below_row, left_col, visited_matrix, new_region)

            # diagonal below right
            if right_col < len(visited_matrix[0]):
                find_all_connected_cells(
                    below_row, right_col, visited_matrix, new_region)

        # left
        if left_col >= 0:
            find_all_connected_cells(
                row, left_col, visited_matrix, new_region)

        # right
        if right_col < len(visited_matrix[0]):
            find_all_connected_cells(
                row, right_col, visited_matrix, new_region)

    regions = []
    visited_matrix = [[False for _ in matrix[0]] for _ in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1 and visited_matrix[row][col] == False:
                new_region = []
                find_all_connected_cells(row, col, visited_matrix, new_region)
                regions.append(new_region)

    if len(regions) > 0:
        return max(map(lambda x: len(x), regions))
    else:
        return 0


def print_matrix(matrix):
    for row in matrix:
        print(row)


matrix1 = [
    [1, 1, 0],
    [1, 0, 0],
    [0, 0, 1]
]  # 3
matrix2 = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
]  # 5

row_len = random.randint(1, 5)
col_len = row_len

rand_matrix = [[random.randint(0, 1) for _ in range(col_len)]
               for _ in range(row_len)]
print_matrix(rand_matrix)
print(max_num_of_connected_cells_in_matrix(rand_matrix))

print(max_num_of_connected_cells_in_matrix(matrix1))
print(max_num_of_connected_cells_in_matrix(matrix2))
