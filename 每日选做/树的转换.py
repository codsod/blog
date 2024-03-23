class BinaryNode:

    def __init__(self):
        self.children = []
        self.leftChild = None
        self.rightSibling = None


def DFSbuid(exp):
    stack = []
    node = BinaryNode()
    stack.append(node)
    for char in exp:
        if char == 'd':
            node = BinaryNode()
            stack[-1].children.append(node)
            stack.append(node)
        elif char == 'u':
            stack.pop()
    return stack[0]


def LCRStree(node):
    if node.children:
        node.leftChild = node.children[0]
        for index in range(len(node.children) - 1):
            node.children[index].rightSibling = node.children[index + 1]
            LCRStree(node.children[index])
        LCRStree(node.children[-1])


def DFSdepth(node):
    if not node.children:
        return 0
    return max(DFSdepth(child) for child in node.children) + 1


def LCRSdepth(node):
    if node == None:
        return -1
    return max(LCRSdepth(node.leftChild), LCRSdepth(node.rightSibling)) + 1


exp = input()
root = DFSbuid(exp)
LCRStree(root)
print(f"{DFSdepth(root)} => {LCRSdepth(root)}")
