# INPUT_FILE = "./input-example.txt"
INPUT_FILE = "./input.txt"


def get_all_steps(vectors):
    steps = []
    for v in vectors:
        if v[0] not in steps:
            steps.append(v[0])
        if v[1] not in steps:
            steps.append(v[1])
    return steps


def get_available_steps(remaining_steps, ongoing_steps, vectors):
    steps = []
    for s in remaining_steps:
        if s not in [v[1] for v in vectors] and s not in [os["letter"] for os in ongoing_steps] and s not in steps:
            steps.append(s)
    return steps


def update_vectors(vectors, step):
    for i in reversed(range(len(vectors))):
        if step == vectors[i][0] or step == vectors[i][1]:
            del vectors[i]


vectors = [(l[5], l[36]) for l in open(INPUT_FILE)]
TIME_OFFSET = 60

available_workers = 5

all_steps = get_all_steps(vectors)
remaining_steps = all_steps
available_steps = []
ongoing_steps = []

time_elapsed = 0
while True:
    available_steps = get_available_steps(
        remaining_steps, ongoing_steps, vectors)

    for w in range(available_workers):
        if (available_steps):
            ongoing_steps.append({
                "letter": available_steps[0],
                "time_remaining": TIME_OFFSET + (ord(available_steps[0]) - 64)
            })
            del available_steps[0]
            available_workers -= 1

    for i in reversed(range(len(ongoing_steps))):
        letter = ongoing_steps[i]["letter"]

        ongoing_steps[i]["time_remaining"] -= 1
        if (ongoing_steps[i]["time_remaining"] == 0):
            del ongoing_steps[i]
            remaining_steps.remove(letter)
            update_vectors(vectors, letter)
            available_workers += 1

    time_elapsed += 1
    if (len(remaining_steps) == 0):
        print("Time elapsed: {}".format(time_elapsed))
        break
