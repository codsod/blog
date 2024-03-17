class Stack:
    def __init__(self):
        self.items = []
        self.stack_size=0

    def isEmpty(self):
        return self.stack_size==0
    
    def push(self,newitem):
        self.items.append(newitem)
        self.stack_size+=1

    def pop(self):
        self.stack_size-=1
        return self.items.pop()
    
    def peek(self):
        return self.items[self.stack_size-1]
    
    def size(self):
        return self.stack_size
    
class BinaryTree:
    def __init__(self,root) :
        self.key = root
        self.left=None
        self.right=None
    
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.left=self.left
            self.left=t

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.right=self.right
            self.right=t
    
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def getRoot(self):
        return self.key
    
    def setRoot(self,obj):
        self.key=obj

    def traversal(self,method='preorder'):
        if method == 'preorder':
            print(self.key,end=" ")
        if self.left!=None:
            self.left.traversal(method)
        if method =='inorder':
            print(self.key,end=" ")
        if self.right !=None:
            self.right.traversal(method)
        if method =='postorder':
            print(self.key,end=" ")

def buildParseTree(fpexp):
    fplist=fpexp.split()
    pStack=Stack()
    eTree=BinaryTree('')
    pStack.push(eTree)
    currentTree =eTree

    for i in fplist:
        if i=='(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree =currentTree.getLeft()
        elif i not in '+-*/)':
            currentTree.setRoot(int(i))
            parent =pStack.pop()
            currentTree =parent
        elif i in '+-*/':
            currentTree.setRoot(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRight()
        elif i == ')':
            currentTree =pStack.pop()
        else:
            raise ValueError("Unknown Operator:"+i)
    return eTree

exp = "( ( 7 + 3 ) * ( 5 - 2 ) )"
pt= buildParseTree(exp)
for mode in ['preorder','inorder','postorder']:
    pt.traversal(mode)
    print()
        

