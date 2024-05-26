def connected(graph,vn):
    visited=[0]*vn
    queue=[]
    queue.append(0)
    visited[0]=1
    while queue:
        u=queue.pop(0)
        for i in graph[u]:
            if visited[i]==0:
                visited[i]=1
                queue.append(i)
    if 0 in visited:
        return False
    else:
        return True
def loop(graph,vn):
    visited=[0]*vn
    for i in range(vn):
        if visited[i]==0:
            queue=[]
            last=-1
            queue.append((i,last))
            visited[i]=1
            while queue:
                u,last=queue.pop(0)
                for j in graph[u]:
                    if visited[j]==0:
                        visited[j]=1
                        queue.append((j,u))
                    elif visited[j]==1:
                        if j!=last:
                            return True
                        else:
                            continue
    return False

vn,en=map(int,input().split())
graph=[[] for i in range(vn)]
for i in range(en):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
if connected(graph,vn):
    print("connected:yes")
else:
    print("connected:no")
if loop (graph,vn):
    print("loop:yes")
else:
    print("loop:no")
