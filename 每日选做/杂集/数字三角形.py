def maxsolve(a,b):
    global n
    if a==n-1:
        return tri[a][b]
    if c[a][b]>0:
        return c[a][b]

    c[a][b]=tri[a][b]+max(maxsolve(a+1,b),maxsolve(a+1,b+1))
    return c[a][b]


n = int(input())
c = [[0] * n for _ in range(n)]
tri=[]
for _ in range(n):
    tri.append(list(map(int,input().split())))
print(maxsolve(0,0))
