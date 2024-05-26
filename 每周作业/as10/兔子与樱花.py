import heapq
import math
def dijkstra(g,st,end):
    if st ==end:return[]
    dist={i:(math.inf,[]) for i in g}
    dist[st]=(0,[st])
    pos=[]
    heapq.heappush(pos,(0,st,[]))
    while pos:
        dist1,cur,path=heapq.heappop(pos)
        for next,dist2 in g[cur].items():
            if dist2 +dist1 <dist[next][0]:
                dist[next]=(dist2+dist1,path+[next])
                heapq.heappush(pos,(dist2+dist1,next,path+[next]))
    return dist[end][1]

n=int(input())
g={input():{} for _ in range(n)}
for _ in range(int(input())):
    p1,p2,dist=input().split()
    g[p1][p2]=int(dist)
    g[p2][p1]=int(dist)
for _ in range(int(input())):
    st,end=input().split()
    path=dijkstra(g,st,end)
    s=st
    cur=st
    for i in path:
        s += f'->({g[cur][i]})->{i}'
        cur=i
    print(s)