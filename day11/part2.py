INPUT_FILE = "./input.txt"

GRID_SIZE = 300


def compute_cell_power_lvl(x, y, grid_sn):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_sn
    power_level *= rack_id
    power_str = str(power_level)
    if len(power_str) < 3:
        power_level = 0
    else:
        power_level = int(power_str[-3])
    power_level -= 5

    return power_level


def populate_grid_with_cell_power(grid, grid_sn):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            grid[y][x] = compute_cell_power_lvl(x, y, grid_sn)


def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print('\n')


def find_biggest_sm(grid):
    sizes = []

    for sm_size in range(1, GRID_SIZE + 1):
        strip_sum = [[0 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

        for x in range(GRID_SIZE):
            total = 0
            for y in range(sm_size):
                total += grid[y][x]
                strip_sum[0][x] = total

            for y in range(1, GRID_SIZE - sm_size + 1):
                total += grid[y + sm_size - 1][x] - grid[y - 1][x]
                strip_sum[y][x] = total

        max_sum = -100
        for y in range(GRID_SIZE - sm_size + 1):
            total = 0
            for x in range(sm_size):
                total += strip_sum[y][x]

            if (total > max_sum):
                max_sum = total
                position = (0, y)

            for x in range(1, GRID_SIZE - sm_size - 1):
                total += strip_sum[y][x + sm_size - 1] - strip_sum[y][x - 1]
                if total > max_sum:
                    max_sum = total
                    position = (x, y)

        sizes.append({"position": position, "size":  sm_size, "sum": max_sum})

    biggest = sorted(sizes, key=lambda s: s["sum"])[-1]
    return (biggest["position"], biggest["size"])


grid_sn = int(open(INPUT_FILE).read().strip('\n'))
fuel_grid = [[0 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

populate_grid_with_cell_power(fuel_grid, grid_sn)
position, size = find_biggest_sm(fuel_grid)
print("Top-left corner: {}".format(position))
print("Size: {}".format(size))
