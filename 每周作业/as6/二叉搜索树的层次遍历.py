from collections import defaultdict


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def treeinsert(node, item):
    if node is None:
        return Node(item)
    if item < node.key:
        node.left = treeinsert(node.left, item)
    elif item > node.key:
        node.right = treeinsert(node.right, item)
    return node


def BFS(node):
    stack = [node]
    order = []
    while stack:
        node = stack.pop(0)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        order.append(node.key)
    return order


a = defaultdict()
temp = list(map(int, input().strip().split()))
order = []
root = Node(temp[0])
for i in range(1, len(temp)):
    if temp[i] not in a:
        a[temp[i]] = 1
        treeinsert(root, temp[i])
c = BFS(root)
print(*c)
