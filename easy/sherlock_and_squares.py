import math
import random

def squares(start, end):
    i = 1
    nb_squares = 0
    while i**2 <= end:
        if i**2 >= start:
            nb_squares += 1
        i += 1
    
    return nb_squares


def squares2(start, end):
    return math.floor(math.sqrt(end)) - math.floor(math.sqrt(start))


test1 = [24, 49] # 25, 36, 49
test2 = [3, 9] # 4, 9
test3 = [17, 24] # 0
a = random.randint(1, 100)
b = random.randint(a, 200)
test4 = [a, b]
print(test4)

print(squares(*test1), squares2(*test1))
print(squares(*test2), squares2(*test2))
print(squares(*test3), squares2(*test3))
print(squares(*test4), squares2(*test4))