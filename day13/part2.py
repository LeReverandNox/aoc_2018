# INPUT_FILE = "./input_example2.txt"
INPUT_FILE = "./input.txt"

FILE = open(INPUT_FILE)


class Cart:
    def __init__(self, symbol, x, y, line_w):
        self._intersectionMoves = [-90, 0, 90]
        self._intersectionCounter = 0

        self.orientation = self._getDegFromSymbol(symbol)
        self.x = x
        self.y = y
        self.grid_position = x + y * line_w
        self.deleted = False

    def _getDegFromSymbol(self, symbol):
        if symbol == '^':
            return 0
        if symbol == 'v':
            return 180
        if symbol == '<':
            return 270
        if symbol == '>':
            return 90

    def _getSymbol(self):
        if self.orientation == 0:
            return '^'
        if self.orientation == 180:
            return 'v'
        if self.orientation == 270:
            return '<'
        if self.orientation == 90:
            return '>'

    def _getIntersectionOrientation(self):
        move = self._intersectionMoves[self._intersectionCounter % 3]
        self._intersectionCounter += 1

        return move

    def _getDefaultMove(self):
        if self.orientation == 0:
            return 0, -1
        if self.orientation == 180:
            return 0, 1
        if self.orientation == 270:
            return -1, 0
        if self.orientation == 90:
            return 1, 0

    def _getTurnOrientation(self, symbol):
        if symbol == '/':
            if self.orientation == 0 or self.orientation == 180:
                return 90
            else:
                return -90
        elif symbol == '\\':
            if self.orientation == 0 or self.orientation == 180:
                return -90
            else:
                return 90

    def move(self, grid):
        next_x, next_y = self._getDefaultMove()

        grid[self.y][self.x]["player"] = None

        self.x += next_x
        self.y += next_y
        curr_cell = grid[self.y][self.x]

        if curr_cell["player"] != None:
            grid[self.y][self.x]["player"] = None
            return False

        if curr_cell["road"] == '+':
            self.orientation = (self.orientation +
                                self._getIntersectionOrientation()) % 360
        elif curr_cell["road"] in ['/', '\\']:
            self.orientation = (self.orientation +
                                self._getTurnOrientation(curr_cell["road"])) % 360

        grid[self.y][self.x]["player"] = self._getSymbol()
        return True


def parse_input(f):
    grid = []
    carts = []

    for y, row in enumerate(f.readlines()):
        grid_row = []
        for x, cell in enumerate(row.rstrip('\n')):
            if cell in ['^', 'v', '<', '>']:
                cart = Cart(cell, x, y, len(row))
                carts.append(cart)
                grid_row.append({"road": '?', "player": cell})
            else:
                grid_row.append({"road": cell, "player": None})

        grid.append(grid_row)

    return grid, carts


def sort_carts(carts):
    return sorted([c for c in carts if c.deleted is False], key=lambda c: c.grid_position)


def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell["player"]:
                print(cell["player"], end="")
            else:
                print(cell["road"], end="")
        print()


def print_carts(carts):
    for i, c in enumerate(carts):
        print("Cart {}".format(i))
        print("({}, {})".format(c.x, c.y))
        print("Position on the grid: {}".format(c.grid_position))
        print('\n')


grid, carts = parse_input(FILE)


def delete_carts_at_pos(carts, x, y):
    for c in carts:
        if c.x == x and c.y == y:
            c.deleted = True


def get_last_cart(carts):
    for c in carts:
        if c.deleted is False:
            return c


def count_remaining_carts(carts):
    return sum([1 for c in carts if c.deleted is False])


def loop(grid, carts):
    while True:
        carts = sort_carts(carts)

        if count_remaining_carts(carts) == 1:
            last_cart = get_last_cart(carts)
            return last_cart.x, last_cart.y

        for i, c in enumerate(carts):
            if c.deleted is False:
                if not c.move(grid):
                    delete_carts_at_pos(carts, c.x, c.y)


print(loop(grid, carts))
