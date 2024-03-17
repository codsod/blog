class Nodes:
    def __init__(self,value):
        self.value = value
        self.children = []

def tree_build(nodes):
    parentstack = []
    node=None
    
    for i in nodes:
        if i.isalpha():
            node=Nodes(i)
            if parentstack:
                parentstack[-1].children.append(node)
        elif i == '(':
            if node:
                parentstack.append(node)
        elif i == ')':
            if parentstack:
                node=parentstack.pop()
    return node

def preorder(node):
    output=[node.value]
    for child in node.children:
        output.extend(preorder(child))
    return ''.join(output)

def postorder(node):
    output=[]
    for childe in node.children:
        output.extend(postorder(childe))
    output.append(node.value)
    return ''.join(output)

nodes=input().strip()
nodes=''.join(nodes.split())
root=tree_build(nodes)
print(preorder(root))
print(postorder(root))