class Node:
    def __init__(self):
        self.left = None
        self.right = None

def treeheight(Node):
    if Node == None:
        return -1
    left=treeheight(Node.left)
    right=treeheight(Node.right)
    return max(left,right)+1

def count_leaves(node):
    if node== None:
        return 0
    if node.left == None and node.right == None:
        return 1
    return count_leaves(node.left)+count_leaves(node.right)

n=int(input())
nodes=[Node() for i in range(n)]
has_parent=[False for i in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    if a!=-1:
        nodes[i].left=nodes[a]
        has_parent[a]=True
    if b!=-1:
        nodes[i].right=nodes[b]
        has_parent[b]=True

roor_index=has_parent.index(False)
root=nodes[roor_index]

height=treeheight(root)
leaves=count_leaves(root)

print(f"{height} {leaves}")