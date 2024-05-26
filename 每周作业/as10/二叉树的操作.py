class Node:
    def __init__(self,key):
        self.key = key
        self.left=None
        self.right=None

def build_tree(nodesl):
    nodes=[Node(i) for i in range(n)]
    for key,left,right in nodesl:
        if left!=-1:
            nodes[key].left=nodes[left]
        if right!=-1:
            nodes[key].right=nodes[right]
    return nodes
def swap(nodes,x,y):# 交换操作
    for node in nodes:
        if node.left and node.left.key in [x,y]:
            if node.left.key==x:
                node.left=nodes[y]
            else:
                node.left=nodes[x]
        if node.right and node.right.key in [x,y]:
            if node.right.key==x:
                node.right=nodes[y]
            else:
                node.right=nodes[x]
def find_leftmost(node): # 找到左子树最左的节点
    while node and node.left:
        node=node.left
    return node.key if node else -1

for _ in range(int(input())):
    n,m=map(int,input().split())
    nodesl=[tuple(map(int,input().split())) for _ in range(n)]
    ops=[tuple(map(int,input().split())) for _ in range(m)]
    nodes=build_tree(nodesl)
    for op in ops:
        if op[0]==1:
            swap(nodes,op[1],op[2])
        elif op[0]==2:
            print(find_leftmost(nodes[op[1]]))

