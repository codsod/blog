class Node:
    def __init__(self, val):
        self.children = []
        self.val = val


def mintraverse(_node):
    if not _node.children:
        return [_node.val]
    stack = [_node] + _node.children
    res = []
    stack.sort(key=lambda x: x.val)
    for tree in stack:
        if tree == _node:
            res.append(tree.val)
        else:
            res.extend(mintraverse(tree))
    return res


n = int(input())
parent = [0] * n
treestack = []
indexstack = []
for _ in range(n):
    trs = list(map(int, input().split()))
    if trs[0] not in indexstack:
        node = Node(trs[0])
        treestack.append(node)
        indexstack.append(trs[0])
    else:
        ind = indexstack.index(trs[0])
        node = treestack[ind]
    for i in range(1, len(trs)):
        if trs[i] not in indexstack:
            chnode = Node(trs[i])
            node.children.append(chnode)
            treestack.append(chnode)
            indexstack.append(trs[i])
            parent[len(treestack) - 1] = 1
        else:
            ind = indexstack.index(trs[i])
            node.children.append(treestack[ind])
            parent[ind] = 1
indexroot = parent.index(0)
root = treestack[indexroot]
order = mintraverse(root)
for i in order:
    print(i)
