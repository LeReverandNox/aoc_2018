import re

INPUT_FILE = "./input.txt"
# INPUT_FILE = "./input_example.txt"


def generate_node(datas):
    node = {
        "children": [],
        "nb_children": datas[0],
        "metadatas": [],
        "nb_metadatas": datas[1]
    }

    children_length = 2
    for n in range(node["nb_children"]):
        child, length = generate_node(datas[children_length:])
        children_length += length
        node["children"].append(child)

    for n in range(node["nb_metadatas"]):
        node["metadatas"].append(datas[n + children_length])

    return node, (children_length + node["nb_metadatas"])


def compute_node_value(node):
    if not node["children"]:
        node["value"] = sum(node["metadatas"])
    else:
        node["value"] = 0

        for m in node["metadatas"]:
            if (m - 1) < len(node["children"]):
                node["value"] += compute_node_value(node["children"][m - 1])

    return node["value"]


datas = [int(n)
         for n in re.findall("\d+", open(INPUT_FILE).read().rstrip('\n'))]


root, _ = generate_node(datas)
root_value = compute_node_value(root)

print(root_value)
