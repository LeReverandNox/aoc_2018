import re
import collections

# INPUT_FILE = "./input-example.txt"
INPUT_FILE = "./input.txt"
MODIFIER = 100


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None

    def print(self):
        if not self.first:
            return

        current = self.first
        while True:
            print(current.data)
            current = current.next
            if (current == self.first):
                break

    def insertAfterNode(self, prev_node, data):
        node = Node(data)
        node.prev = prev_node
        node.next = prev_node.next
        node.next.prev = node
        prev_node.next = node
        return node

    def insertAtEnd(self, data):
        if not self.first:
            node = Node(data)
            self.first = node
            node.next = node
            node.prev = node
        else:
            self.insertAfterNode(self.first.prev, data)

    def removeNode(self, node):
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.first == node:
                self.first = node.next

    def getRelativeNodeByIndex(self, ref_node, index):
        if index == 0:
            return ref_node

        if index < 0:
            current = ref_node.prev
            for i in range(abs(index) - 1):
                current = current.prev
            return current

        elif index > 0:
            current = ref_node.next
            for i in range(index - 1):
                current = current.next

            return current


games = [{"players": int(m[0]), "marbles": int(m[1]) * MODIFIER}
         for m in [re.findall("\d+", l) for l in open(INPUT_FILE).readlines()]]


for g in games:
    board_list = CircularDoublyLinkedList()
    board_list.insertAtEnd(0)

    scores = collections.defaultdict(int)
    current_m = board_list.first

    for m in range(1, g["marbles"] + 1):
        if m % 23 == 0:
            next_m = board_list.getRelativeNodeByIndex(current_m, -7)
            scores[m % g["players"]] += (m + next_m.data)
            board_list.removeNode(next_m)
            next_m = next_m.next
        else:
            next_m = board_list.insertAfterNode(current_m.next, m)
        current_m = next_m

    print(max(scores.values()))
