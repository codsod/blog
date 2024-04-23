from collections import deque


class Vertex:

    def __init__(self, id):
        self.id = id
        self.connectedto = {}
        self.distance = 2**63 - 1
        self.previous = None
        self.situ = 0
        # 0 未访问 1 已访问 2 访问中
    def addnbr(self, nbr, weight=0):
        self.connectedto[nbr] = weight

    def getnbr(self):
        return self.connectedto.keys()


class Graph:

    def __init__(self):
        self.vertexlist = {}
        self.number = 0

    def addvertex(self, key):
        self.number += 1
        newv = Vertex(key)
        self.vertexlist[key] = newv
        return newv

    def getvertex(self, key):
        if key in self.vertexlist:
            return self.vertexlist[key]
        else:
            return None

    def __len__(self):
        return self.number

    def __contains__(self, n):
        return n in self.vertexlist

    def addedge(self, a, b, weight=0):
        if a not in self.vertexlist:
            nv = self.addvertex(a)
        if b not in self.vertexlist:
            nv = self.addvertex(b)
        self.vertexlist[a].addnbr(self.vertexlist[b], weight)

    def getvertexs(self):
        return list(self.vertexlist.keys())

    def __iter__(self):
        return iter(self.vertexlist.values())


def build_graph(words):
    buckets = {}
    the_graph = Graph()
    for word in words:
        for i, _ in enumerate(word):
            bucket = f"{word[:i]}_{word[i+1:]}"
            buckets.setdefault(bucket, set()).add(word)
    for siw in buckets.values():
        for word1 in siw:
            for word2 in siw - {word1}:
                the_graph.addedge(word1, word2)
    return the_graph


n = int(input())
words = [input() for _ in range(n)]
g = build_graph(words)


def bfs(start):
    start.distance = 0
    start.previous = None
    vque = deque([start])
    while len(vque):
        v = vque.popleft()
        for nbr in v.getnbr():
            if nbr.situ == 0:
                nbr.situ = 2
                nbr.distance = v.distance + 1
                nbr.previous = v
                vque.append(nbr)
        v.situ = 1


def traverse(end):
    ans = []
    current = end
    while (current.previous):
        ans.append(current.id)
        current = current.previous
    ans.append(current.id)
    return ans[::-1]


start, end = input().split()
bfs(g.getvertex(start))
if end in g and g.getvertex(end).situ == 1:
    ans = traverse(g.getvertex(end))
    print(*ans)
else:
    print("NO")
