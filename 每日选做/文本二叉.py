class Node:
    def __init__(self,char,len):
        self.char=char
        self.len=len
        self.left=None
        self.right=None

def file_buildtree(files):
    stack=[]
    node=Node(files.pop(0),1)
    stack.append(node)
    for char in files:
        node=Node(char[-1],len(char))
        while stack and stack[-1].len>=node.len:
            stack.pop()
        if stack[-1].left:
            stack[-1].right=node
        else:
            stack[-1].left=node
        stack.append(node)
    return stack[0]
            
def traversal(node,method):
    traver=[]
    if node and node.char!='*':
        if method=='preorder':
            traver.append(node.char)
        traver.extend(traversal(node.left,method))
        if method=='inorder':
            traver.append(node.char)
        traver.extend(traversal(node.right,method))
        if method=='postorder':
            traver.append(node.char)
    return traver

files=[]
n=int(input())
for _ in range(n):
    while True:
        line=input()
        if line=='0':
            root=file_buildtree(files)
            print(''.join(traversal(root,'preorder')))
            print(''.join(traversal(root,'postorder')))
            print(''.join(traversal(root,'inorder')))
            print()
            files=[]
            break
        else:
            files.append(line)
