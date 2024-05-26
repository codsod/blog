n,m=map(int,input().split())
total=n+1
tree=[1 for i in range(total)]
for _ in range(m):
    st,ed=map(int,input().split())
    for i in range(st,ed+1):
        tree[i]=0
t=sum(tree[i] for i in range(total))
print(t)