def surface_area(item):
    def get_above_and_below_surface():
        return len(item) * len(item[0]) * 2

    def get_x_axis_surface():
        x_surface = 0
        i = 0
        prev_sizes = [0 for _ in item[0]]
        while i < len(item):
            for j in range(len(item[0])):
                size = item[i][j]
                visible_surface = size - prev_sizes[j]
                if visible_surface > 0:
                    x_surface += visible_surface

                prev_sizes[j] = size

            i += 1

        return x_surface

    def get_reverse_x_axis_surface():
        rev_x_surface = 0
        i = len(item) - 1
        prev_sizes = [0 for size in item[0]]
        while i >= 0:
            for j in range(len(item[0])):
                size = item[i][j]
                visible_surface = size - prev_sizes[j]
                if visible_surface > 0:
                    rev_x_surface += visible_surface

                prev_sizes[j] = size

            i -= 1

        return rev_x_surface

    def get_y_axis_surface():
        y_surface = 0
        j = 0
        prev_sizes = [0 for size in item]
        while j < len(item[0]):
            col = []
            for i in range(len(item)):
                size = item[i][j]
                col.append(size)
                visible_surface = size - prev_sizes[i]
                if visible_surface > 0:
                    y_surface += visible_surface

            prev_sizes = col

            j += 1

        return y_surface

    def get_reverse_y_axis_surface():
        y_surface = 0
        j = len(item[0]) - 1
        prev_sizes = [0 for size in item]
        while j >= 0:
            col = []
            for i in range(len(item)):
                size = item[i][j]
                col.append(size)
                visible_surface = size - prev_sizes[i]
                if visible_surface > 0:
                    y_surface += visible_surface

            prev_sizes = col

            j -= 1

        return y_surface

    surface = 0

    surface += get_above_and_below_surface()
    surface += get_x_axis_surface()
    surface += get_reverse_x_axis_surface()
    surface += get_y_axis_surface()
    surface += get_reverse_y_axis_surface()

    return surface


test1 = [[1]]  # 6
test2 = [[1, 3, 4], [2, 2, 3], [1, 2, 4]]  # 60

print(surface_area(test1))
print(surface_area(test2))
