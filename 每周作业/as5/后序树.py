class Node:

    def __init__(self, char):
        self.char = char
        self.left = None
        self.right = None


def PostTree(line):
    nodestack = []
    for char in line:
        if char.islower():
            node = Node(char)
            nodestack.append(node)
        elif char.isupper():
            node = Node(char)
            node.right = nodestack.pop()
            node.left = nodestack.pop()
            nodestack.append(node)
    return nodestack.pop()


def queueorder(root):
    queue = [root]
    rever = []
    while queue:
        node = queue.pop(0)
        rever.append(node.char)
        if node.left and node.right:
            queue.append(node.left)
            queue.append(node.right)
    queor = reversed(rever)
    return ''.join(queor)


n = int(input())
for _ in range(n):
    line = input()
    root = PostTree(line)
    print(queueorder(root))
