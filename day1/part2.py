INPUT = "input.txt"

changes = [int(line.rstrip('\n')) for line in open(INPUT)]
frequencies = []
base = 0


not_found = True
while not_found:
    for change in changes:
        base += change
        if base in frequencies:
            not_found = False
            print(base)
            break
        else:
            frequencies.append(base)
