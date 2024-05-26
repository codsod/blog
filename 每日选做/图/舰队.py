def dfs(node,color):
    color[node]=1
    for neigh in graph[node]:
        if color[neigh]==1:
            return True
        if color[neigh]==0 and dfs(neigh,color):
            return True
    color[node]=2
    return False

T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    graph=[[] for i in range(n)]
    flag=False
    for i in range(m):
        a,b=map(int,input().split())
        graph[a-1].append(b-1)
    color=[0]*(n)
    for i in range(n):
        if color[i]==0:
            if dfs(i,color):
                flag=True
                break
    print("Yes" if flag else "No")