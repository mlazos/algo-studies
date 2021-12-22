
from collections import deque, defaultdict


class TrieNode:
    def __init__(self, children=None, valid=False):
        self.valid = valid
        self.children = children if children else defaultdict(TrieNode)


def construct_trie(words):
    root = TrieNode()
    root.char = ""

    for word in words:
        cur_node = root
        for char in word:
            cur_node = cur_node.children[char]
            cur_node.char = char
        cur_node.valid = True

    return root


def print_trie(root):
    stack = deque([(node, 0) for node in root.children.values()])

    cur_depth = 0
    while stack:
        cur_node, depth = stack.pop()

        surrounding = "|" if cur_node.valid else " "
        print(surrounding + cur_node.char + surrounding, end="")

        if len(cur_node.children) == 0:
            print("")
            if stack:
                print("".join(["   "] * stack[-1][1]), end="")

        for child in cur_node.children.values():
            stack.append((child, depth + 1))


trie = construct_trie(["hi", "my", "name", "is", "Mike", "miner",
                       "hello", "her", "his", "mine", "Michael"])

print_trie(trie)
