class Node:

    def __init__(self, char):
        self.char = char
        self.children = []


def build_tree(exp):
    stack = []
    for i in exp:
        if i.isalpha():
            node = Node(i)
            if stack:
                stack[-1].children.append(node)
        elif i == '(':
            stack.append(node)
        elif i == ')':
            node=stack.pop()

    return node


def preorder(root):
    if root:
        print(root.char, end='')
        for child in root.children:
            preorder(child)


def postorder(root):
    if root:
        for child in root.children:
            postorder(child)
        print(root.char, end='')


exp = input()
root = build_tree(exp)
preorder(root)
print()
postorder(root)
