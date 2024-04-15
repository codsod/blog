class Vertex:
    def __init__(self,key):
        self.id=key
        self.nbrs={}
    def getid(self):
        return self.id
    def gerconnect(self):
        return self.nbrs.keys()
class Graph:
    def __init__(self):
        self.vertlist={}
        self.num=0
    def addVertex(self,key):
        self.num+=1
        newvert=Vertex(key)
        self.vertlist[key]=newvert
        return newvert
    def addEdge(self,a,b,weight=0):
        if a not in self.vertlist:
            n=self.addVertex(a)
        if b not in self.vertlist:
            m=self.addVertex(b)
        self.vertlist[a].nbrs[self.vertlist[b]]=weight
        self.vertlist[b].nbrs[self.vertlist[a]]=weight
    def __iter__(self):
        return iter(self.vertlist.values())
    
def lapalas(n, edges):
    g = Graph()
    lap = []
    for i in range(n):
        g.addVertex(i)
    for edge in edges:
        g.addEdge(edge[0], edge[1])
        g.addEdge(edge[1], edge[0])
    for vertex in g:
        row = [0] * n
        row[vertex.getid()] = len(vertex.gerconnect())
        for nbr in vertex.gerconnect():
            row[nbr.getid()] = -1
        lap.append(row)
    return lap


n, m = map(int, input().split())
edges = []
for i in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

laplacianMatrix = lapalas(n, edges)

for row in laplacianMatrix:
    print(' '.join(map(str, row)))
