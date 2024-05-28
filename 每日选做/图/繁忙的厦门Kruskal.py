import heapq

class Disjoint:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rx=self.find(x)
        ry=self.find(y)

        if rx!=ry:
            if self.rank[rx]<self.rank[ry]:
                self.parent[rx]=ry
            elif self.rank[rx]>self.rank[ry]:
                self.parent[ry]=rx
            else:
                self.parent[ry]=rx
                self.rank[rx]+=1

def kruskal(graph):
    n=len(graph)
    joint=Disjoint(n)

    edges=[(score,x,y) for x in range(n) for y,score in graph[x].items()]
    heapq.heapify(edges)

    edgesnum=0

    while edges:
        scor,x,y=heapq.heappop(edges)
        if joint.find(x)!=joint.find(y):
            joint.union(x,y)
            edgesnum+=1
            maxscore=scor

    return (edgesnum,maxscore)


n, m = map(int, input().split())
graph = {i: {} for i in range(n)}
for _ in range(m):
    a, b, score = map(int, input().split())
    graph[a - 1][b - 1] = score
    graph[b - 1][a - 1] = score
p = kruskal(graph)
print(*p)
