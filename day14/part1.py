from collections import deque

# INPUT = 9
INPUT = 165061

d = deque([3, 7])

n1 = 0
n2 = 1
while len(d) < (INPUT + 10):
    n1 = (n1 + d[n1] + 1) % len(d)
    n2 = (n2 + d[n2] + 1) % len(d)
    new_recipe = str(d[n1] + d[n2])
    for i in new_recipe:
        d.append(int(i))


for i in range(10):
    print(d[INPUT+i], end="")
print('\n')
