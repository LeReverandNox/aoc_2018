INPUT = "input.txt"

changes = [int(line.rstrip('\n')) for line in open(INPUT)]
base = 0

print(sum(changes, 0))
