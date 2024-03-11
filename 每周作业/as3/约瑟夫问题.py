from collections import deque
def out_list(num,first,m):
    list=deque()
    outlist=[]
    for i in range(num):
        list.append(i+1)
    
    for i in range(first-1):
        list.append(list.popleft())
    
    while len(list)>1:
        for index in range(m-1):
            list.append(list.popleft())
        outlist.append(str(list.popleft()))
    outlist.append(str(list.pop()))
    return outlist

while True:
    n,p,m=map(int,input().split())
    if n==0 and m==0 and p==0:
        break
    outlist=out_list(n,p,m)
    print(",".join(outlist))
