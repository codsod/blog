class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildtree(exp):
    root = None
    stack = []
    oper = []
    number = ''
    for j in range(len(exp)):
        i = exp[j]
        if i.isnumeric() or i=='-':
            number += i
        else:
            if number:
                node = Node(int(number))
                number = ''
                if stack:
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                stack.append(node)
            if i == '(':
                oper.append(i)
            elif i == ')':
                if exp[j - 1] == '(':
                    oper.pop()
                else:
                    oper.pop()
                    root = stack.pop()
    return root


def sum(root, val):
    global target
    if root is None:
        return False
    if root.left is None and root.right is None:
        return val + root.val == target

    return sum(root.left, val + root.val) or sum(root.right, val + root.val)
def bracket(exp):
    stack=[]
    for i in exp:
        if i=='(':
            stack.append(i)
        elif i==')':
            stack.pop()
    if not stack:
        return True
    else:
        return False


def summing(exp):
    root = buildtree(exp)
    if sum(root, 0):
        print('yes')
    else:
        print('no')

while True:
    try:
        s=input()
        space=s.index(' ')
        target=int(s[:space])
        exp=s[space+1:]
        while not bracket(exp):
            sp=input()
            exp+=sp
        summing(exp)
    except:
        break
