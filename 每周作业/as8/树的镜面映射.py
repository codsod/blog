class Node:
    def __init__(self,char,weight):
        self.char = char
        self.left = None
        self.right = None
        self.children = []
        self.weight=weight
def build_tree(nodes):
    stack=[]
    for node in nodes:
        if not stack:
            stack.append(node)
            continue
        if stack:
            while len(stack)>=2 and stack[-1].left and stack[-1].right:
                stack.pop()
            if not stack[-1].left:
                stack[-1].left=node
            elif not stack[-1].right:
                stack[-1].right=node
            if node.weight=='0':
                stack.append(node)
    return stack[0]
def turntree(node):
    if not node.left and not node.right:
        return
    if node.left!='$' :
        turntree(node.left)
    if node.right!='$' :
        turntree(node.right)
    targe=node.left
    while  targe!=None:
        if targe.char=='$':
            break
        node.children.append(targe)
        targe=targe.right
def niBFS(root):
    queue=[]
    queue.append(root)
    while queue:
        node=queue.pop(0)
        print(node.char,end=' ')
        for child in node.children[::-1]:
            queue.append(child)
            
n=int(input())
nodes=[Node(o[0],o[1]) for o in input().split()]
root=build_tree(nodes)
turntree(root)
niBFS(root)

    