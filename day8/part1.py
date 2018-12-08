import re

INPUT_FILE = "./input.txt"
# INPUT_FILE = "./input_example.txt"

INDEX = 1


def parse_datas(datas):
    global INDEX
    node = {
        "index": INDEX,
        "children": [],
        "nb_children": datas[0],
        "metadatas": [],
        "nb_metadatas": datas[1]
    }
    INDEX += 1

    children_length = 2
    for n in range(node["nb_children"]):
        child, length = parse_datas(datas[children_length:])
        children_length += length
        node["children"].append(child)

    for n in range(node["nb_metadatas"]):
        node["metadatas"].append(datas[n + children_length])

    return node, (children_length + node["nb_metadatas"])


def flatten(l):
    return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]


def compute_metadatas_sum(node):
    return sum(flatten(node["metadatas"] + [flatten(compute_metadatas_sum(n))
                                            for n in node["children"]]))


datas = [int(n)
         for n in re.findall("\d+", open(INPUT_FILE).read().rstrip('\n'))]


root, _ = parse_datas(datas)
sum_metadatas = compute_metadatas_sum(root)

print(sum_metadatas)
