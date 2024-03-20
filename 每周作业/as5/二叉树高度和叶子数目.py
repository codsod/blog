class Node:

    def __init__(self):
        self.left = None
        self.right = None


def height_tree(root):
    if root == None:
        return -1
    return max(height_tree(root.left), height_tree(root.right)) + 1


def leaves_tree(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    return leaves_tree(root.left) + leaves_tree(root.right)


n = int(input())
have_parent = [False for _ in range(n)]
nodes = [Node() for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    if a != -1:
        nodes[i].left = nodes[a]
        have_parent[a] = True
    if b != -1:
        nodes[i].right = nodes[b]
        have_parent[b] = True

rootindex = have_parent.index(False)
root = nodes[rootindex]
print(height_tree(root), leaves_tree(root))
