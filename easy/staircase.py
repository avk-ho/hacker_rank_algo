# https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true

import random

def staircase(n):
    def print_staircase_stage(n, i, chr):
        space = " "

        print(f"{space * (n - i)}" + f"{chr * i}")


    staircase_character = "#"

    for i in range(1, n + 1):
        print_staircase_stage(n, i, staircase_character)

max_n = 10
n = random.randint(1, max_n)
print(n)
staircase(n)