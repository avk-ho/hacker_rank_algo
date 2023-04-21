# https://www.hackerrank.com/challenges/an-interesting-game-1/problem?isFullScreen=true


def gaming_array(arr):
    # Bob is True, Andy is False
    winning_player = False
    while len(arr) > 0:
        max_num = max(arr)
        max_num_idx = arr.index(max_num)
        
        arr = arr[:max_num_idx]
        winning_player = not winning_player
    
    if winning_player:
        return "Bob"
    else:
        return "Andy"


arr1 = [2, 3, 5, 4, 1] # Bob
arr2 = [5, 2, 6, 3, 4] # Andy
arr3 = [3, 1] # Bob
arr4 = [1, 3, 5, 7, 9] # Bob
arr5 = [7, 4, 6, 5, 9] # Andy

print(gaming_array(arr1))
print(gaming_array(arr2))
print(gaming_array(arr3))
print(gaming_array(arr4))
print(gaming_array(arr5))