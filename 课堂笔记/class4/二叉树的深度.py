class Node:
    def __init__(self):
        self.left = None
        self.right = None
def treedepth(Node):
    if Node==None:
        return 0
    left=treedepth(Node.left)
    right=treedepth(Node.right)
    return max(left,right)+1

n=int(input())
nodes=[Node() for i in range(n)]

for i in range(n):
    lef,rig=map(int,input().split())
    if lef!=-1:
        nodes[i].left=nodes[lef-1]
    if rig!=-1:
        nodes[i].right=nodes[rig-1]
root =nodes[0]
depth=treedepth(root)
print(depth)