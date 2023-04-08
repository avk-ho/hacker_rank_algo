# https://www.hackerrank.com/challenges/palindrome-index/problem?isFullScreen=true

def palindrome_index(st):
    def verify_palindrome(st):
        i, j = 0, len(st) - 1
        is_palindrome = True
        while i < j:
            is_palindrome = st[i] == st[j]
            
            if not is_palindrome:
                break
            
            i += 1
            j -= 1

        return is_palindrome


    i = 0
    while i < len(st):
        temp_list = list(st)
        temp_list.pop(i)
        print(temp_list)

        if verify_palindrome(temp_list):
            break

        i += 1
    
    if i >= len(st):
        return -1
    else:
        return i


test1 = "bcbc"
test2 = "aaab"
test3 = "baa"
test4 = "bocb"
test5 = "abcde"

print(palindrome_index(test1))
print(palindrome_index(test2))
print(palindrome_index(test3))
print(palindrome_index(test4))
print(palindrome_index(test5))