import heapq

def prim(graph,start):
    roadnum=0
    scorelist=[]
    visited=set([start])
    edges=[(cost,start,to) for to,cost in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        cost,a,b=heapq.heappop(edges)
        if b not in visited:
            visited.add(b)
            roadnum+=1
            scorelist.append(cost)
            for to,cost in graph[b].items():
                if to not in visited:
                    heapq.heappush(edges,(cost,b,to))
    maxscore=max(scorelist)

    return (roadnum,maxscore)

n,m=map(int,input().split())
graph={i:{} for i in range(n)}
for _ in range(m):
    a,b,score=map(int,input().split())
    graph[a - 1][b - 1] = score
    graph[b - 1][a - 1] = score
p=prim(graph,0)
print(*p)
