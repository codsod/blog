def find(i):
    if parent[i]!=i:
        parent[i]=find(parent[i])
    return parent[i]

def union(i,j):
    parentx =find(i)
    parenty =find(j)
    if parentx!=parenty:
        parent[parenty]=parentx
        
while True:
    try:
        n,m=map(int,input().split())
        parent=list(range(n+1))
        
        for _ in range(m):
            a,b =map(int,input().split())
            if find(a)==find(b):
                print("Yes")
            else:
                print("No")
                union(a,b)
        have=set()
        for i in range(1,n+1):
            have.add(find(i))
        ans=sorted(have)
        print(len(ans))
        print(*ans)
        
    except EOFError:
        break