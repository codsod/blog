class Node:

    def __init__(self, key):
        self.id = key
        self.left = None
        self.right = None


def buildtree(marks):
    stack = []
    for mark in marks:
        if stack:
            while stack[-1].left and stack[-1].right:
                stack.pop()
            if stack[-1].left == None:
                stack[-1].left = Node(mark)
                stack.append(stack[-1].left)
            elif stack[-1].right == None:
                stack[-1].right = Node(mark)
                stack.append(stack[-1].right)
        else:
            stack.append(Node(mark))
        if stack[-1].id == ".":
            stack.pop()
    return stack[0]


def traverse(node, method):
    if node:
        if method == 'pre' and node.id != '.':
            print(node.id, end='')
        traverse(node.left, method)
        if method == 'in' and node.id != '.':
            print(node.id, end='')
        traverse(node.right, method)
        if method == 'post' and node.id != '.':
            print(node.id, end='')


marks = input()
root = buildtree(marks)
traverse(root, 'in')
print()
traverse(root, 'post')
