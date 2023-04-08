# https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true

# 2 operations possible: 
# append a letter at the end of the string
# delete a letter at the end of the string

def append_and_delete(start, target, nb_operations):
    i = 0
    while i < len(start) and i < len(target) and target[i] == start[i]:
        i += 1
    
    delete_operations = len(start) - i
    add_operations = len(target) - i
    
    return (add_operations + delete_operations) <= nb_operations


test1 = [["a", "b", "c"], ["d", "e", "f"], 6]
test2 = ["hackerhappy", "hackerrank", 9]
test3 = ["ashley", "ash", 2]

print(append_and_delete(*test1))
print(append_and_delete(*test2))
print(append_and_delete(*test3))