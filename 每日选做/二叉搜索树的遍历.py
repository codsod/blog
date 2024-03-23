class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def searchtree(preorder):
    stack = []
    is_root = True
    for key in preorder:
        node = Node(key)
        if stack and stack[-1].key > node.key:
            stack[-1].left = node
        if stack and stack[-1].key < node.key:
            while stack and stack[-1].key < node.key:
                parent = stack.pop()
                if not stack and is_root:
                    root = parent
                    is_root = False
            parent.right = node
        stack.append(node)
    return root


def traversal(node, method):
    DFS = ['pre', 'in', 'post']
    traver = []
    if method in DFS:
        if node:
            if method == 'pre':
                traver.append(node.key)
            traver.extend(traversal(node.left, method))
            if method == 'in':
                traver.append(node.key)
            traver.extend(traversal(node.right, method))
            if method == 'post':
                traver.append(node.key)
    return traver


n = int(input())
datas = list(map(int, input().split()))
root = searchtree(datas)
post = traversal(root, 'post')
print(*post)
