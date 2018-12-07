import jellyfish as jf

INPUT = "./input.txt"
ids = [idee.rstrip('\n') for idee in open(INPUT)]

for idee in ids:
    for candidate in ids:
        if jf.levenshtein_distance(idee, candidate) == 1:
            answer = ""
            for i, c in enumerate(idee):
                if c == candidate[i]:
                    answer += c

print(answer)
