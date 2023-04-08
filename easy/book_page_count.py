# https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true

# page 1 always on the right page (0 | 1)
# n pages in the book, p target page

# p = (2 * x) + 1

def minimum_pages_turned(n, p):
    nb_pages_from_start = 0
    nb_pages_from_end = 0
    
    # current_page_from_start = 1
    # current_page_from_end = n

    visible_from_start = [0, 1]
    if n % 2 == 0:
        visible_from_end = [n, n+1]
    else:
        visible_from_end = [n-1, n]


    while not p in visible_from_start and not p in visible_from_end:
        visible_from_start = list(map(lambda x: x+2, visible_from_start))
        visible_from_end = list(map(lambda x: x-2, visible_from_end))
        nb_pages_from_start += 1
        nb_pages_from_end += 1

        # print(visible_from_start)
        # print(visible_from_end)

    return min(nb_pages_from_start, nb_pages_from_end)


print(minimum_pages_turned(7, 3))
print(minimum_pages_turned(5, 3))
print(minimum_pages_turned(6, 2))
print(minimum_pages_turned(5, 4))