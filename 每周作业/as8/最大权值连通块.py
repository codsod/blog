class Vertex:
    def __init__(self,key):
        self.id=key
        self.connected={}
        self.weight=0
    def addweight(self,value):
        self.weight=value
class Graph:
    def __init__(self):
        self.vertlist={}
        self.num=0
    def addVertex(self,key):
        self.num+=1
        newv=Vertex(key)
        self.vertlist[key]=newv
        return newv
    def addEdge(self,a,b):
        if a not in self.vertlist.keys():
            self.addVertex(a)
        if b not in self.vertlist.keys():
            self.addVertex(b)
        va=self.vertlist[a]
        vb=self.vertlist[b]
        self.vertlist[a].connected[vb]=1
        self.vertlist[b].connected[va]=1
sum=0
maxs=0
def dfs(v):
    global sum
    if v.weight==0:
        return
    sum+=v.weight
    v.weight=0
    for nbr in v.connected:
        dfs(nbr)
n,m=map(int,input().split())
g=Graph()
for i in range(n):
    g.addVertex(i)
for i,value in enumerate(input().split()):
    g.vertlist[i].addweight(int(value))
for _ in range(m):
    a,b=map(int,input().split())
    g.addEdge(a,b)
for vertex in g.vertlist.values():
    if vertex.weight!=0:
        sum=0
        dfs(vertex)
        maxs=max(maxs,sum)
print(maxs)
    