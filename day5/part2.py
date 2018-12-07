import string

INPUT = "./input.txt"

polymer = open(INPUT).read().rstrip('\n')


def compute_polymer_length(polymer):
    i = 0
    while i < len(polymer):
        curr_c = polymer[i] if i < len(polymer) else ''
        next_c = polymer[i + 1] if i + 1 < len(polymer) else ''
        if not next_c or not curr_c:
            break
        if ((curr_c.islower() and next_c.isupper())
                or (curr_c.isupper() and next_c.islower())) and curr_c.lower() == next_c.lower():
            polymer = polymer[:i] + polymer[i + 2:]
            if (i > 0):
                i -= 1
        else:
            i += 1
    return len(polymer)


polymer_lengths = []
for c in string.ascii_lowercase:
    polymer_cp = polymer
    polymer_cp = polymer_cp.replace(c, '')
    polymer_cp = polymer_cp.replace(c.upper(), '')
    polymer_lengths.append(compute_polymer_length(polymer_cp))

print("Le polymer le plus court mesure {}".format(min(polymer_lengths)))
