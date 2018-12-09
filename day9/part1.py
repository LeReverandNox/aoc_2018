import re
import collections

# INPUT_FILE = "./input-example.txt"
INPUT_FILE = "./input.txt"

games = [{"players": int(m[0]), "marbles": int(m[1])}
         for m in [re.findall("\d+", l) for l in open(INPUT_FILE).readlines()]]

for g in games:
    board = [0, 2, 1]
    scores = collections.defaultdict(int)
    current_m = 1

    for m in range(3, g["marbles"] + 1):
        curr_player = ((m - 1) % g["players"]) + 1

        if m % 23 == 0:
            scores[curr_player] += m
            next_m = (current_m - 7) % len(board)
            scores[curr_player] += board[next_m]
            del board[next_m]
        else:
            next_m = current_m + 2

            if next_m == len(board):
                board.append(m)
            elif next_m > len(board):
                board.insert(1, m)
                next_m = 1
            else:
                board.insert(next_m, m)
        current_m = next_m

    print(max(scores.values()))
