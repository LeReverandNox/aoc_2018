INPUT = "./input.txt"


def compute_manhattan_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def compute_total_distance(cell):
    total_distance = 0
    for c in COORDINATES:
        total_distance += compute_manhattan_distance(cell, c["coords"])
    return total_distance


def compute_safe_locations_with_correct_distance():
    safe_locations = 0

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if compute_total_distance((x, y)) < MAX_DISTANCE:
                safe_locations += 1
    return safe_locations


COORDINATES = [{"index": i, "coords": (int(s[0]), int(s[1]))}
               for i, s in enumerate([c.split(',') for c in open(INPUT)])]
MAX_DISTANCE = 10000

# COORDINATES = [
#     {"index": 0, "coords": (1, 1)},
#     {"index": 1, "coords": (1, 6)},
#     {"index": 2, "coords": (8, 3)},
#     {"index": 3, "coords": (3, 4)},
#     {"index": 4, "coords": (5, 5)},
#     {"index": 5, "coords": (8, 9)}
# ]
# MAX_DISTANCE = 32


max_x = max([c["coords"][1] for c in COORDINATES]) + 1
max_y = max([c["coords"][0] for c in COORDINATES]) + 1
GRID_SIZE = max([max_x, max_y])

safe_locations = compute_safe_locations_with_correct_distance()
print(safe_locations)
