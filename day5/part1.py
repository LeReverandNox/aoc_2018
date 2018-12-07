INPUT = "./input.txt"

polymer = open(INPUT).read().rstrip('\n')

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

print("Le polymer restant mesure {}".format(len(polymer)))
