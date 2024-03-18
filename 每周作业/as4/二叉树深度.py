class Node:
    def __init__(self):
        self.left=None
        self.right=None

def tree_depth(node):
    if node==None:
        return 0
    left=tree_depth(node.left)
    right=tree_depth(node.right)
    return max(left,right)+1

n=int(input())
nodes=[Node() for _ in range(n)]
parent=[-1]*n
for i in range(n):
    leftindex,rightindex=map(int,input().split())
    if leftindex!=-1:
        nodes[i].left=nodes[leftindex-1]
        parent[leftindex-1]=i
    if rightindex!=-1:
        nodes[i].right=nodes[rightindex-1]
        parent[rightindex-1]=i

rootindex=parent.index(-1)
root=nodes[rootindex]
print(tree_depth(root))