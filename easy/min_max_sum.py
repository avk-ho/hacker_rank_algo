import random

def mini_max_sum(arr):
    min_elem = None
    max_elem = None
    sum_arr = 0
    for elem in arr:
        if min_elem is None or max_elem is None:
            min_elem = elem
            max_elem = elem
        
        if elem < min_elem:
            min_elem = elem
        elif elem > max_elem:
            max_elem = elem
        
        sum_arr += elem
    
    return [sum_arr - max_elem, sum_arr - min_elem]


def mini_max_sum2(arr):
    sorted_arr = sorted(arr)

    return [sum(sorted_arr[:-1]), sum(sorted_arr[1:])]


nb_int = 5
arr = [random.randint(1, 9) for _ in range(nb_int)]
print(arr)

print(mini_max_sum(arr))
print(mini_max_sum2(arr))