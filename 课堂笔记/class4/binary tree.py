from collections import deque

class Node:
    def __init__(self,key):
        self.child=[]
        self.key=key

def NewNode(key):
    temp=Node(key)
    return temp

def levelorder(root):
    if(root==None):
        return
    q=deque()
    q.append(root)
    while(len(q)!=0):
        n=len(q)
        while(n>0):
            p=q[0]
            q.popleft()
            print(p.key,end=" ")
            for i in range(len(p.child)):
                q.append(p.child[i])
            n=n-1
        print()