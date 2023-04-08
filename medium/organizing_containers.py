# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true

def organize_containers(*args):
    containers = [container for container in args]
    total_per_idx = {}
    switch_capacity = {}
    
    idx = 0
    while idx < len(containers):
        container = containers[idx]
        switch_capacity[idx] = sum(container)
        for j in range(len(container)):
            total_per_idx[j] = total_per_idx.get(j, 0) + container[j]
            
        idx += 1
            
    # print(total_per_idx.items())
    # print(switch_capacity.items())
    total_values = list(total_per_idx.values())
    switch_values = list(switch_capacity.values())
    total_values.sort()
    switch_values.sort()
    
    if total_values == switch_values:
        return True
    else:
        return False
    
    
c1 = [1, 4]
c2 = [2, 3]

c1a = [1, 6]
c2a = [2, 1]

c3 = [1, 3, 1]
c4 = [2, 1, 2]
c5 = [3, 3, 3]

c6 = [1, 1]
c7 = [1, 1]

c8 = [0, 2, 1]
c9 = [1, 1, 1]
c0 = [2, 0, 0]
# 0 2 1     1 2 0   0 3 0
# 2 1 0     2 1 0   3 0 0
# 1 0 1     0 0 2   0 0 2

test1 = [c1, c2] # False
test2 = [c1a, c2a] # True
test3 = [c3, c4, c5] # False
test4 = [c6, c7] # True
test5 = [c8, c9, c0] # True

print(organize_containers(c1, c2))
print(organize_containers(*test2))
print(organize_containers(*test3))
print(organize_containers(*test4))
print(organize_containers(*test5))