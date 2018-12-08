# INPUT_FILE = "./input-example.txt"
INPUT_FILE = "./input.txt"

vectors = [(l[5], l[36]) for l in open(INPUT_FILE)]


def get_list_steps(vectors):
    if not vectors:
        return [s for s in all_steps if s not in ordered_steps]
    steps = set()

    for v in vectors:
        steps.add(v[0])
        steps.add(v[1])

    return steps


def remove_vector_involving_step(vectors, step):
    return [v for v in vectors if step != v[0] and step != v[1]]


def find_next_step(steps, vectors):
    next_steps = []
    for s in steps:
        if s not in [v[1] for v in vectors]:
            next_steps.append(s)
    return sorted(next_steps)[0]


ordered_steps = []
all_steps = get_list_steps(vectors)

while True:
    steps = get_list_steps(vectors)
    if len(steps) == 1:
        ordered_steps.append(steps[0])
        break
    next_step = find_next_step(steps, vectors)
    ordered_steps.append(next_step)
    vectors = remove_vector_involving_step(vectors, next_step)

print("".join(ordered_steps))
