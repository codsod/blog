def find(x):
    if x != parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    parent[find(x)]=find(y)

casenum=0
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    count=0
    parent=[i for i in range(n+1)]
    for _ in range(m):
        x,y=map(int,input().split())
        union(x,y)
    for i in range(n):
        if find(i)==i:
            count+=1
    casenum+=1
    print(f"Case {casenum}: {count}")