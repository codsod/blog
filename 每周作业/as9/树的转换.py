class Node:
    def __init__(self):
        self.children = []
        self.leftson=None
        self.rightb=None
    def normalheight(self):
        if self.children:
            return 1+max(child.normalheight() for child in self.children)
        else:
            return 0
    def binaryheight(self):
        if self.leftson and self.rightb:
            return 1+max(self.leftson.binaryheight(),self.rightb.binaryheight())
        elif self.leftson:
            return 1+self.leftson.binaryheight()
        elif self.rightb:
            return 1+self.rightb.binaryheight()
        else:
            return 0
def buildtree(marks):
    root=Node()
    stack=[root]
    for mark in marks:
        if mark=='d':
            newnode=Node()
            stack[-1].children.append(newnode)
            stack.append(newnode)
        elif mark=='u':
            stack.pop()
    return stack[0]
def normaltobinary(node):
    if node.children:
        node.leftson=node.children[0]
        for childin in range(len(node.children)):
            if childin ==len(node.children)-1:
                normaltobinary(node.children[childin])
                break
            else:
                node.children[childin].rightb=node.children[childin+1]
                normaltobinary(node.children[childin])
marks=input()
root=buildtree(marks)
normaltobinary(root)
a=root.normalheight()
b=root.binaryheight()
print(f"{a} => {b}")
