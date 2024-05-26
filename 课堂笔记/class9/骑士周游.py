import sys
class Graph:
    def __init__(self):
        self.vertices={}
        self.number=0
    def add_vertex(self,key):
        self.number+=1
        nv=Vertex(key)
        self.vertices[key]=nv
        return nv
    def get_vertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None
    def __len__(self):
        return self.number
    def __contains__(self,n):
        return n in self.vertices
    def add_edge(self,a,b,weight=0):
        if a not in self.vertices:
            nv=self.add_vertex(a)
        if b not in self.vertices:
            nv=self.add_vertex(b)
        self.vertices[a].add_neighbor(self.vertices[b],weight)
    def getvertex(self):
        return self.vertices.keys()
    def __iter__(self):
        return iter(self.vertices.values())
class Vertex:
    def __init__(self,num):
        self.key=num
        self.connectedto={}
        self.color='white'
        self.distance=sys.maxsize
        self.previous=None
        self.disc=0
        self.fin=0
    def __lt__(self,o):
        return self.key<o.key
    def add_neighbor(self,nbr,weight=0):
        self.connectedto[nbr]=weight
    def get_neighbors(self):
        return self.connectedto.keys()
def pos_to_node(row,col,n):
    return row*n+col
def gen_moves(row,col,n):
    new_moves=[]
    move_offsets=[(1,-2),(1,2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    for dr,dc in move_offsets:
        if (0<=row+dr<n and 0<=col+dc<n):
            new_moves.append((row+dr,col+dc))
    return new_moves
def knight_graph(n):
    g=Graph()
    for row in range(n):
        for col in range(n):
            node_id=pos_to_node(row,col,n)
            new_positions=gen_moves(row,col,n)
            for row2,col2 in new_positions:
                other_node=pos_to_node(row2,col2,n)
                g.add_edge(node_id,other_node)
    return g
def ordered_by_avail(u):
    res_list=[]
    for v in u.get_neighbors():
        if v.color=='white':
            c=0
            for w in v.get_neighbors():
                if w.color=='white':
                    c+=1
            res_list.append((c,v))
    res_list.sort(key=lambda x:x[0])
    return [y[1] for y in res_list]
            
def knight_tour(n,path,u,limit):
    u.color='gray'
    path.append(u)
    if n<limit:
        neighbors=ordered_by_avail(u)
        i=0
        for nbr in neighbors:
            if nbr.color =='white' and knight_tour(n+1,path,nbr,limit):
                return True
        else:
            path.pop()
            u.color='white'
            return False
    else:
        return True

def NodeToPos(id):
    return ((id//8,id%8))
bdsize=int(input())
*start_pos,=map(int,input().split())
g=knight_graph(bdsize)
start_vertex=g.get_vertex(pos_to_node(start_pos[0],start_pos[1],bdsize))
if start_pos is None:
    print("fail")
    exit(0)
tour_path=[]
done=knight_tour(0,tour_path,start_vertex,len(g))
if done:
    print('success')
else:
    print('fail')
exit(0)