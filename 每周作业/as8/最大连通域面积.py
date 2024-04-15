s=0
def search(i,j):
    global s
    if matrix[i][j]=='.':
        return
    s+=1
    matrix[i][j]='.'
    for ai in range(-1,2):
        for aj in range(-1,2):
            if ai==0 and aj==0:
                continue
            search(i+ai,j+aj)
                
dat=int(input())
for _ in range(dat):
    maxs=0
    n,m=map(int,input().split())
    matrix=[['.' for _ in range(m+2)]for _ in range(n+2)]
    for i in range(1,n+1):
        matrix[i][1:-1]=input()
    for i in range(1,n+1):
        for j in range(1,m+1):
            if matrix[i][j]=='W':
                s=0
                search(i,j)
                maxs=max(maxs,s)
    print(maxs)