# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem?isFullScreen=true

def min_number_of_transmitters(map, radio_range):
    def update_radio_coverage(idx):
        next_idx = idx + 1
        while next_idx < len(sorted_map):
            next_house_pos = sorted_map[next_idx]

            if next_house_pos - current_house_pos <= radio_range:
                coverage_map[next_idx] = True
                next_idx += 1
            else:
                break

    sorted_map = sorted(map)
    coverage_map = [False for _ in sorted_map]

    nb_transmitters = 0

    idx = 0
    current_earliest_house_covered_idx = 0

    while False in coverage_map and idx < len(sorted_map):
        current_house_pos = sorted_map[idx]
        house_is_covered = coverage_map[idx]

        if house_is_covered:
            # moving the previous transmitter to that position
            # would break coverage of a previous house
            if current_house_pos - sorted_map[current_earliest_house_covered_idx] > radio_range:
                idx += 1
                continue

        else:
            # install a new transmitter
            nb_transmitters += 1
            coverage_map[idx] = True
            current_earliest_house_covered_idx = idx

        update_radio_coverage(idx)

        # print(idx, coverage_map)
        idx += 1

    return nb_transmitters


map1, range1 = [1, 2, 3, 5, 9], 1  # 3
map2, range2 = [1, 2, 3, 4, 5], 1  # 2
map3, range3 = [7, 2, 4, 6, 5, 9, 12, 11], 2  # 3
map4, range4 = [1, 3, 5], 2  # 1
map5, range5 = [7], 1  # 1

print(min_number_of_transmitters(map1, range1))
print(min_number_of_transmitters(map2, range2))
print(min_number_of_transmitters(map3, range3))
print(min_number_of_transmitters(map4, range4))
print(min_number_of_transmitters(map5, range5))

# idx 0, transm = 1 // 1, 2 covered, early 0
# idx 1, transm = 1 // 1, 2, 3 covered, early 0
# idx 2, transm = 1 // 1, 2, 3 covered, early 0
# idx 3, transm = 2 // 1, 2, 3, 5 covered, early 5
# idx 4, transm = 3 // 1, 2, 3, 5, 9 covered, early 9