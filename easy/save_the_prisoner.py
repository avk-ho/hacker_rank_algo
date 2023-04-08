# https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true

def save_the_prisoner(nb_prisoners, nb_sweets, starting_chair):
    current_chair = starting_chair
    nb_sweets -= 1
    while nb_sweets > 0:
        if current_chair % nb_prisoners == 0:
            current_chair = 1
        else:
            current_chair += 1
        nb_sweets -= 1

    return current_chair

test1 = [4, 6, 2] # 2 3 4 1 2 3
test2 = [5, 2, 1] # 1 2
test3 = [5, 2, 2] # 2 3
test4 = [7, 19, 2] # 6
test5 = [3, 7, 3] # 3

print(save_the_prisoner(*test1))
print(save_the_prisoner(*test2))
print(save_the_prisoner(*test3))
print(save_the_prisoner(*test4))
print(save_the_prisoner(*test5))