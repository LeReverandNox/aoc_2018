INPUT_FILE = "./input.txt"
# INPUT_FILE = "./input_example.txt"

GENERATIONS = 20


def pad_state(state, offset):
    while state[:5] != ".....":
        state = '.' + state
        offset += 1
    while state[-5:] != ".....":
        state += '.'
    return state, offset


def is_sequence_in_rules(seq, rules):
    for r in rules:
        if seq == r["pattern"]:
            return r["result"]
    return '.'


file = open(INPUT_FILE)
state = file.readline()[15:].rstrip('\n')
file.readline()
rules = [{
    "pattern": s[0:5],
    "result": s[9]
} for s in file.readlines()]


offset = 0
state, offset = pad_state(state, offset)

for g in range(1, GENERATIONS + 1):
    new_state = ['.', '.']
    for i in range(2, len(state) - 2):
        pots = state[i - 2:i + 3]
        c_pot = is_sequence_in_rules(pots, rules)
        new_state.append(c_pot)
    state, offset = pad_state("".join(new_state), offset)

total = 0
for i, p in enumerate(state):
    if p == '#':
        total += i - offset

print(total)
