from collections import defaultdict
INPUT = "input.txt"

ids = [id.rstrip('\n') for id in open(INPUT)]
twoLetters = 0
threeLetters = 0

for id in ids:
    foundTwo = False
    foundThree = False
    chars = defaultdict(int)
    for char in id:
        chars[char] += 1
    for char, nb in chars.items():
        if nb == 2 and not foundTwo:
            twoLetters += 1
            foundTwo = True
        if nb == 3 and not foundThree:
            threeLetters += 1
            foundThree = True

print(twoLetters * threeLetters)
