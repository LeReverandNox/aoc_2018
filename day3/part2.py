import re

INPUT = "./input.txt"
GRID_SIZE = 1000


def init_grid(size):
    return [[0 for x in range(size)] for y in range(size)]


def parse_inputs(lines):
    claims = []
    for raw_claim in inputs:
        matches = re.search('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', raw_claim)
        claim = {}
        claim["Id"] = int(matches.group(1))
        claim["x"] = int(matches.group(2))
        claim["y"] = int(matches.group(3))
        claim["w"] = int(matches.group(4))
        claim["h"] = int(matches.group(5))
        claims.append(claim)
    return claims


def fill_grid(grid, claims):
    for claim in claims:
        for x in range(claim["x"], claim["x"] + claim["w"]):
            for y in range(claim["y"], claim["y"] + claim["h"]):
                grid[x][y] += 1


def find_not_overlaped_claim(grid, claims):
    for claim in claims:
        overlaped = False
        for x in range(claim["x"], claim["x"] + claim["w"]):
            for y in range(claim["y"], claim["y"] + claim["h"]):
                if (grid[x][y] > 1):
                    overlaped = True
                    break
        if not overlaped:
            return claim["Id"]


inputs = [line.rstrip('\n') for line in open(INPUT)]
claims = parse_inputs(inputs)
grid = init_grid(GRID_SIZE)
fill_grid(grid, claims)
print(find_not_overlaped_claim(grid, claims))
