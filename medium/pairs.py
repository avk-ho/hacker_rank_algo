# https://www.hackerrank.com/challenges/pairs/problem?isFullScreen=true

def pairs(target, arr):
    pairs = []
    
    sorted_arr = list(reversed(sorted(arr)))
    
    i = 0
    while i < len(sorted_arr) - 1:
        j = len(sorted_arr) - 1
        
        while j > i:
            pair_result = sorted_arr[i] - sorted_arr[j]
            
            if pair_result == target:
                pairs.append((sorted_arr[i], sorted_arr[j]))
            if pair_result < target:
                break
            
            j -= 1
        
        i += 1
    
    # print(pairs)
    return len(pairs)


target1, arr1 = 1, [1, 2, 3, 4] # 3
target2, arr2 = 2, [1, 5, 3, 4, 2] # 3

print(pairs(target1, arr1))
print(pairs(target2, arr2))