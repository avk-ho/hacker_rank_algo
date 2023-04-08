import random

# s is start of the house
# t is the endpoint of the house
# a is the position of the apple tree
# b is the position of the orange tree
# apples and oranges lists contains distances d where they fall

# a < s < t < b

def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apples_in_house = 0
    oranges_in_house = 0

    for apple_distance in apples:
        if s <= (a + apple_distance) <= t:
            apples_in_house += 1
        
    for orange_distance in oranges:
        if s <= (b + orange_distance) <= t:
            oranges_in_house += 1

    return apples_in_house, oranges_in_house


dist_diff = 10
nb_apples = 5
nb_oranges = 5
a = random.randint(1, dist_diff)
s = random.randint(a + 1, a + 1 + dist_diff)
t = random.randint(s + 1, s + 1 + dist_diff)
b = random.randint(t + 1, t + 1 + dist_diff)
apples = [random.randint(-dist_diff, dist_diff) for _ in range(nb_apples)]
oranges = [random.randint(-dist_diff, dist_diff) for _ in range(nb_oranges)]
print(a, s, t, b)
print(apples)
print(oranges)
print(count_apples_and_oranges(s, t, a, b, apples, oranges))