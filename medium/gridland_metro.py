# https://www.hackerrank.com/challenges/gridland-metro/problem?isFullScreen=true

# tracks is a list of [row, start_col, end_col]

def num_of_unoccupied_cells(num_rows, num_cols, tracks):
    matrix = [[1 for _ in range(num_cols)] for _ in range(num_rows)]
    
    for track in tracks:
        row, start_col, end_col = track[0] - 1, track[1] - 1, track[2] - 1
        
        for col in range(start_col, end_col + 1):
            matrix[row][col] = 0
        
    return sum(map(lambda x: sum(x), matrix))


test1 = 4, 4, [[2, 2, 3], [3, 1, 4], [4, 4, 4]] # 9
test2 = 4, 4, [[1, 1, 4], [2, 2, 4], [3, 1, 2], [4, 2, 3]] # 5

print(num_of_unoccupied_cells(*test1))
print(num_of_unoccupied_cells(*test2))
