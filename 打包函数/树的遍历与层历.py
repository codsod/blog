class Node:
    def __init__(self,char):
        self.char=char
        self.children=[]
        self.left=None
        self.right=None
def traversal(node,method):
    DFS=['pre','in','post']
    traver=[]
    if method in DFS:
        if node :
            if method=='pre':
                traver.append(node.char)
            traver.extend(traversal(node.left,method))
            if method=='in':
                traver.append(node.char)
            traver.extend(traversal(node.right,method))
            if method=='post':
                traver.append(node.char)
    if method == 'BFS':
        stack=[node]
        while stack:
            node=stack.pop(0)
            traver.append(node.char)
            for child in node.children:
                stack.append(child)
    return traver

a=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('e')
f=Node('f')
a.left=b
a.right=c
b.children.append(d)
b.children.append(f)
c.children.append(e)
print(''.join(traversal(a,'pre')))
