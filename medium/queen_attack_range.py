# https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true

def queen_attack_range(board_size, queen_coor, obstacles):
    def check_top(new_y):
        return new_y <= board_size

    def check_bot(new_y):
        return new_y > 0

    def check_left(new_x):
        return new_x > 0

    def check_right(new_x):
        return new_x <= board_size

    x, y = queen_coor[0], queen_coor[1]
    distance = 1
    nb_cells = 0

    continue_checking = [True for _ in range(8)]

    while True in continue_checking:
        check_idx = 0
        # top left
        if (
            check_left(x - distance)
            and check_top(y + distance)
            and [x - distance, y + distance] not in obstacles
            and continue_checking[check_idx]
        ):
            nb_cells += 1
        else:
            continue_checking[check_idx] = False

        check_idx += 1

        # top
        if (
            check_top(y + distance)
            and [x, y + distance] not in obstacles
            and continue_checking[check_idx]
        ):
            nb_cells += 1
        else:
            continue_checking[check_idx] = False

        check_idx += 1

        # top right
        if (
            check_right(x + distance)
            and check_top(y + distance)
            and [x + distance, y + distance] not in obstacles
            and continue_checking[check_idx]
        ):
            nb_cells += 1
        else:
            continue_checking[check_idx] = False

        check_idx += 1

        # left
        if (
            check_left(x - distance)
            and [x - distance, y] not in obstacles
            and continue_checking[check_idx]
        ):
            nb_cells += 1
        else:
            continue_checking[check_idx] = False

        check_idx += 1

        # right
        if (
            check_right(x + distance)
            and [x + distance, y] not in obstacles
            and continue_checking[check_idx]
        ):
            nb_cells += 1
        else:
            continue_checking[check_idx] = False

        check_idx += 1

        # bot left
        if (
            check_left(x - distance)
            and check_bot(y - distance)
            and [x - distance, y - distance] not in obstacles
            and continue_checking[check_idx]
        ):
            nb_cells += 1
        else:
            continue_checking[check_idx] = False

        check_idx += 1

        # top
        if (
            check_bot(y - distance)
            and [x, y - distance] not in obstacles
            and continue_checking[check_idx]
        ):
            nb_cells += 1
        else:
            continue_checking[check_idx] = False

        check_idx += 1

        # bot right
        if (
            check_right(x + distance)
            and check_bot(y - distance)
            and [x + distance, y - distance] not in obstacles
            and continue_checking[check_idx]
        ):
            nb_cells += 1
        else:
            continue_checking[check_idx] = False

        distance += 1

    return nb_cells


def recursive_queen_attack_range(board_size, queen_coor, obstacles):
    def check_top(new_y):
        return new_y <= board_size

    def check_bot(new_y):
        return new_y > 0

    def check_left(new_x):
        return new_x > 0

    def check_right(new_x):
        return new_x <= board_size

    def count_top(new_y, cells):
        if check_top(new_y) and [x, new_y] not in obstacles:
            cells += 1
            return count_top(new_y + 1, cells)
        else:
            return cells

    def count_top_left(new_x, new_y, cells):
        if check_top(new_y) and check_left(new_x) and [new_x, new_y] not in obstacles:
            cells += 1
            return count_top_left(new_x - 1, new_y + 1, cells)
        else:
            return cells

    def count_top_right(new_x, new_y, cells):
        if check_top(new_y) and check_right(new_x) and [new_x, new_y] not in obstacles:
            cells += 1
            return count_top_right(new_x + 1, new_y + 1, cells)
        else:
            return cells

    def count_left(new_x, cells):
        if check_left(new_x) and [new_x, y] not in obstacles:
            cells += 1
            return count_left(new_x - 1, cells)
        else:
            return cells

    def count_right(new_x, cells):
        if check_right(new_x) and [new_x, y] not in obstacles:
            cells += 1
            return count_right(new_x + 1, cells)
        else:
            return cells

    def count_bot(new_y, cells):
        if check_bot(new_y) and [x, new_y] not in obstacles:
            cells += 1
            return count_bot(new_y - 1, cells)
        else:
            return cells

    def count_bot_left(new_x, new_y, cells):
        if check_bot(new_y) and check_left(new_x) and [new_x, new_y] not in obstacles:
            cells += 1
            return count_bot_left(new_x - 1, new_y - 1, cells)
        else:
            return cells

    def count_bot_right(new_x, new_y, cells):
        if check_bot(new_y) and check_right(new_x) and [new_x, new_y] not in obstacles:
            cells += 1
            return count_bot_right(new_x + 1, new_y - 1, cells)
        else:
            return cells

    x, y = queen_coor[0], queen_coor[1]

    return (
        count_top(y + 1, 0)
        + count_top_left(x - 1, y + 1, 0)
        + count_top_right(x + 1, y + 1, 0)
        + count_left(x - 1, 0)
        + count_right(x + 1, 0)
        + count_bot(y - 1, 0)
        + count_bot_left(x - 1, y - 1, 0)
        + count_bot_right(x + 1, y - 1, 0)
    )


test1 = [4, [4, 4], []]
test2 = [5, [4, 3], [[5, 5], [4, 2], [2, 3]]]
test3 = [8, [4, 4], [[5, 3]]]
print(
    queen_attack_range(*test1), queen_attack_range(*test2), queen_attack_range(*test3)
)
print(
    recursive_queen_attack_range(*test1),
    recursive_queen_attack_range(*test2),
    recursive_queen_attack_range(*test3),
)
