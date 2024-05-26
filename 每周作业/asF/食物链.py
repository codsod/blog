def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

def check(type,x,y):
    if x>n or y>n:
        return True
    if type==1:
        if find(x+n)==find(y) or find(y+n)==find(x):
            return True
        else:
            p[find(x)]=find(y)
            p[find(x+n)]=find(y+n)
            p[find(x+2*n)]=find(y+2*n)
    elif type==2:
        if find(x)==find(y) or find(y+n)==find(x):
            return True
        else:
            p[find(x+n)]=find(y)
            p[find(x+2*n)]=find(y+n)
            p[find(x)]=find(y+2*n)
    return False



n,k=map(int,input().split())
p=[0]*(3*n+1)
for i in range(3*n+1):
    p[i]=i
num=0
for i in range(k):
    type,x,y=map(int,input().split())
    if check(type,x,y):
        num+=1
print(num)

