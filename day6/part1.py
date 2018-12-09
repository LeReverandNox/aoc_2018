INPUT = "./input.txt"


def init_grid(n):
    return [[-1 for x in range(n)] for y in range(n)]


def compute_manhattan_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def find_closest_coordinate(cell):
    distances = []
    closests = []
    for c in COORDINATES:
        distances.append(
            {"index": c["index"],
             "distance": compute_manhattan_distance(cell, c["coords"])
             })

    distances = (sorted(distances, key=lambda d: d["distance"]))
    for d in distances:
        if not closests or closests[-1]["distance"] == d["distance"]:
            closests.append(d)

    if len(closests) != 1:
        return -1
    return closests[0]["index"]


def populate_grid_with_coords(grid):
    for c in COORDINATES:
        grid[c["coords"][1]][c["coords"][0]] = c["index"]


def populate_grid_with_closests(grid):
    for y in range(grid_size):
        for x in range(grid_size):
            if grid[y][x] != -1:
                continue
            grid[y][x] = find_closest_coordinate((x, y))


def print_grid(grid):
    for row in grid:
        print(row)


def find_border_zones(grid):
    border_zones = set()
    for y in range(grid_size):
        for x in range(grid_size):
            if (y == 0 or y == grid_size - 1 or x == 0 or x == grid_size - 1) and grid[y][x] != '.':
                border_zones.add(grid[y][x])
    return border_zones


def find_possibles_zones(grid):
    possible_zones = []
    border_zones = find_border_zones(grid)
    for c in COORDINATES:
        index = c["index"]
        if index not in border_zones:
            possible_zones.append(index)
    return possible_zones


def compute_zone_sizes(grid, zones):
    zones_sizes = {}
    for z in zones:
        zones_sizes[z] = 0

    for row in grid:
        for cell in row:
            if cell in zones:
                zones_sizes[cell] += 1
    return zones_sizes


def find_biggest_zone(zones):
    return zones[max(zones, key=zones.get)]


COORDINATES = [{"index": i, "coords": (int(s[0]), int(s[1]))}
               for i, s in enumerate([c.split(',') for c in open(INPUT)])]

# COORDINATES = [
#     {"index": 0, "coords": (1, 1)},
#     {"index": 1, "coords": (1, 6)},
#     {"index": 2, "coords": (8, 3)},
#     {"index": 3, "coords": (3, 4)},
#     {"index": 4, "coords": (5, 5)},
#     {"index": 5, "coords": (8, 9)}
# ]

max_x = max([c["coords"][1] for c in COORDINATES]) + 1
max_y = max([c["coords"][0] for c in COORDINATES]) + 1
grid_size = max([max_x, max_y])

grid = init_grid(grid_size)
populate_grid_with_coords(grid)
populate_grid_with_closests(grid)
# print_grid(grid)

possible_zones = find_possibles_zones(grid)
zones_sizes = compute_zone_sizes(grid, possible_zones)
# print(zones_sizes)
biggest_zone = find_biggest_zone(zones_sizes)
print(biggest_zone)
