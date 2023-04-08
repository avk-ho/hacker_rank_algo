# https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

import random

def compareTriplets(a, b):
    n = len(a)
    a_score = 0
    b_score = 0

    for i in range(n):
        if a[i] > b[i]:
            a_score += 1
        elif a[i] < b[i]:
            b_score += 1

    return [a_score, b_score]

a = []
b = []
for i in range(5):
    a.append(random.randint(0, 10))
    b.append(random.randint(0, 10))

print(a, b)
print(compareTriplets(a, b))