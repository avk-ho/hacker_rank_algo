# https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true

import random

def bomberman_game(matrix, t):
    def create_timer_matrix(matrix):
        timer_matrix = []
        for x in range(len(matrix)):
            row = []
            for y in range(len(matrix[0])):
                current_elem = matrix[x][y]
                if current_elem == ".":
                    new_elem = -1
                elif current_elem == "O":
                    new_elem = 4
                
                row.append(new_elem)
                
            timer_matrix.append(row)
            # print(row)
            
        return timer_matrix
    

    def update_matrix(matrix, fill=False):
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                current_timer = matrix[x][y]
                if current_timer > 1:
                    matrix[x][y] = current_timer - 1
                elif current_timer == 1:
                    matrix[x][y] = -1
                    bomb_explosion(x, y)
                elif fill:
                    matrix[x][y] = 3
    
    
    def bomb_explosion(x, y):
        rows = [x - 1, x + 1]
        cols = [y - 1, y + 1]
        
        for row in rows:
            if row < 0 or row >= len(timer_matrix):
                continue
            
            timer_matrix[row][y] = -1
            
        for col in cols:
            if col < 0 or col >= len(timer_matrix[0]):
                continue

            timer_matrix[x][col] = -1


    def recreate_str_matrix(timer_matrix):
        str_matrix = []
        for x in range(len(timer_matrix)):
            row = []
            for y in range(len(timer_matrix[0])):
                current_pos = timer_matrix[x][y]
                if current_pos <= 0:
                    new_elem = "."
                else:
                    new_elem = "O"
                
                row.append(new_elem)
                
            str_matrix.append(row)
            # print(row)
            
        return str_matrix
        
         
    current_t = 0
    timer_matrix = []
    
    while current_t <= t:
        fill = False
        if current_t == 0:
            timer_matrix = create_timer_matrix(matrix)
        
        # every even t, the matrix is filled with bombs
        elif current_t % 2 == 0:
            fill = True
        
        update_matrix(timer_matrix, fill)
        current_t += 1
    
    return recreate_str_matrix(timer_matrix)

# t 0, starter bombs
# t 1, nothing happen
# t 2, all cells without bombs are filled with bombs
# t 3, t0 bombs explode

def create_rand_test(odd_n=False):
    def create_rand_str_base(x, y):
        matrix_str = ""
        # rand_x = random.randint(2, 10)
        # rand_y = random.randint(2, 10)
        # print(rand_x, rand_y)
        
        for i in range(x):
            for j in range(y):
                n = random.randint(1, 10)
                # 20% for a cell of containing a bomb
                if n >= 8:
                    matrix_str += "O"
                else:
                    matrix_str += "."
            matrix_str += "\n"
        
        return matrix_str
    
    
    rand_x = random.randint(2, 10)
    rand_y = random.randint(2, 10)
    if odd_n:
        rand_n = random.randrange(1, 10, 2)
    else:
        rand_n = random.randint(1, 10)
        
    str_base = create_rand_str_base(rand_x, rand_y)
    print(f"x:{rand_x} / y:{rand_y} / n:{rand_n}")
    str_matrix = create_str_matrix(str_base)
    print_matrix(str_matrix)
    
    return str_matrix, rand_n


def create_str_matrix(str):
    matrix = str.split("\n")
    str_matrix = []
    for row in matrix:
        if row == "":
            continue
        
        else:
            new_row = []
            for chr in row:
                new_row.append(chr)
            str_matrix.append(new_row)
        
    return str_matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix1 = [
    [".", ".", "."],
    [".", "O", "."],
    [".", ".", "."]
]

matrix2_str = """
.......
...O...
....O..
.......
OO.....
OO.....
"""
matrix2 = create_str_matrix(matrix2_str)

rand_test = create_rand_test()

print_matrix(bomberman_game(matrix1, 4))
print_matrix(bomberman_game(matrix2, 3))
print_matrix(bomberman_game(*rand_test))