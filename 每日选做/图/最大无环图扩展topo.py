from collections import deque

def maxedge(n,g):
    indegree=[0]*n
    for i in range(n):
        for j in g[i]:
            indegree[j]+=1
    
    topo=[]
    queue=deque([i for i in range(n) if indegree[i]==0])
    while queue:
        node=queue.popleft()
        topo.append(node)
        for nei in g[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                queue.append(nei)
    num=0
    for i in range(n):
        for j in range(i+1,n):
            if topo[j] not in g[topo[i]]:
                num+=1
    return num
    
n,m=map(int,input().split())
edges=set()
g=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    edges.add((a,b))
for a,b in edges:
    g[a].append(b)
print(maxedge(n,g))
