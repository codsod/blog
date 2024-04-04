class Node:
    def __init__(self,char):
        self.char=char
        self.left=None
        self.right=None
        self.str=self._getstr()
    def _getstr(self):
        if  '1' in self.char and '0' not in self.char:
            return 'I'
        elif '0' in self.char and '1' not in self.char:
            return 'B'
        else:
            return 'F'
def buildFBI(line):
    if len(line)==1:
        return Node(line)
    node=Node(line)
    mid=len(line)//2
    node.left=buildFBI(line[:mid])
    node.right=buildFBI(line[mid:])
    return node
def posttraverse(node):
    order=[]
    if node:
        order.extend(posttraverse(node.left))
        order.extend(posttraverse(node.right))
        order.append(node.str)
    return  order
N=int(input())
line=input()
root=buildFBI(line)
print(''.join(posttraverse(root)))
