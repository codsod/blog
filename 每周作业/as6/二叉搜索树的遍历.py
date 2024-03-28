class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def preturn(prefix):
    s = len(prefix)
    if s == 0:
        return None
    node = Node(prefix[0])
    for i in range(1, s):
        if prefix[i] > prefix[0]:
            mid = i
            break
    else:
        mid = s
    left = prefix[1:mid]
    right = prefix[mid:]

    node.left = preturn(left)
    node.right = preturn(right)

    return node


def postorder(root):
    if root == None:
        return []
    order = []
    order.extend(postorder(root.left))
    order.extend(postorder(root.right))
    order.append(root.key)
    return order


n = int(input())
prefix = list(map(int, input().split()))
root = preturn(prefix)
post = postorder(root)
print(*post)
