import random

def grid_search(grid, target):
    def line_search(start_x=0, start_y=0, target_x=0):
        if start_x >= len(grid):
            return False
        
        grid_line = grid[start_x]
        target_line = target[target_x]
        
        y = start_y
        line_present = False
        if len(grid_line) - y >= len(target_line):
            # print(grid_line[y:y+len(target_line)], target_line)
            line_present = grid_line[y:y+len(target_line)] == target_line
        
        return line_present
    
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            temp_x = x
            target_x = 0
            line_present = True
            while target_x < len(target) and line_present:
                line_present = line_search(temp_x, y, target_x)
                
                if line_present:
                    temp_x += 1
                    target_x += 1

            if line_present:
                return True
    
    return False

grid1 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [0, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]
target1 = [
    [8, 7, 6, 5, 4, 3],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

target2 = [
    [1],
    [1]
]

print(grid_search(grid1, target1))
print(grid_search(grid1, target2))

grid_x = random.randint(1, 9)
grid_y = random.randint(1, 9)
target_x = random.randint(1, grid_x)
target_y = random.randint(1, grid_y)

rand_grid = [[random.randint(0, 9) for _ in range(grid_y)] for _ in range(grid_x)]
rand_target = [[random.randint(0, 9) for _ in range(target_y)] for _ in range(target_x)]
print(rand_grid)
print(rand_target)

print(grid_search(rand_grid, rand_target))
# print(grid_search(rand_grid, target2))