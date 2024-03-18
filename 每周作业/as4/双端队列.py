class queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    
    def enqueue(self,item):
        self.items.append(item)
        
    def dequeue(self,type=1):
        if not self.isEmpty():   
            if type==1:
                return self.items.pop()
            if type==0:
                return self.items.pop(0)
        else:
            return 'NULL'
        
t=int(input())
for _ in range(t):
    q=queue()
    ptr=0
    cases=int(input())
    for _ in range(cases):
        kind,type=map(int,input().split())
        if kind==1:
            q.enqueue(type)
        elif kind==2:
            ptr=q.dequeue(type)
        
    if q.isEmpty():
        print('NULL')
    else:
        print(*q.items)



