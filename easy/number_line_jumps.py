# https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true

import random

# x1, x2 are the starting position of each respective kangaroos
# v1, v2 are the distances they reach after 1 jump each respectively
# if they can get at the same position at the same time, return True, else False

# x1 < x2 (the function will work even without this restriction)

def kangaroo(x1, v1, x2, v2):
    # finding which kangaroo starts the more forward, first_k being behind second_k
    if x1 < x2:
        first_k = [x1, v1]
        second_k = [x2, v2]
    else:
        first_k = [x2, v2]
        second_k = [x1, v1]
    
    if first_k == second_k:
        return True

    # first_k can't catch up to second_k
    if first_k[1] <= second_k[1]:
        return False
    
    # both kangaroos jump until first_k gets past/reaches second_k
    while first_k[0] < second_k[0]:
        first_k[0] += first_k[1]
        second_k[0] += second_k[1]
    
    if first_k[0] == second_k[0]:
        return True
    else:
        return False
    
x1, v1 = random.randint(0, 5), random.randint(1, 5)
x2, v2 = random.randint(0, 5), random.randint(1, 5)
print(x1, v1, x2, v2)
print(kangaroo(x1, v1, x2, v2))
print(kangaroo(0, 3, 4, 2)) # must be True