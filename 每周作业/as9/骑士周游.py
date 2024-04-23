import sys


class Graph:

    def __init__(self):
        self.vertices = {}
        self.num = 0

    def add_vertex(self, key):
        self.num += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def __len__(self):
        return len(self.vertices)

    def __contains__(self, n):
        return n in self.vertices

    def add_edge(self, f, t, cost=0):
        if f not in self.vertices:
            nv = self.add_vertex(f)
        if t not in self.vertices:
            nv = self.add_vertex(t)
        self.vertices[f].add_neighbor(self.vertices[t], cost)

    def getVertices(self):
        return list(self.vertices.keys())

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:

    def __init__(self, num):
        self.key = num
        self.connectedTo = {}
        self.color = 'white'
        self.distance = 2**63 - 1
        self.previous = None
        self.disc = 0
        self.fin = 0

    def __lt__(self, o):
        return self.key < o.key

    def add_neighbor(self, nbr, cost=0):
        self.connectedTo[nbr] = cost

    def get_neighbors(self):
        return self.connectedTo.keys()


def knight_graph(board_size):
    kt_graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            node_id = pos_to_node_id(row, col, board_size)
            new_positions = gen_legal_moves(row, col, board_size)
            for row2, col2 in new_positions:
                other_node_id = pos_to_node_id(row2, col2, board_size)
                kt_graph.add_edge(node_id, other_node_id)
    return kt_graph


def gen_legal_moves(row, col, board_size):
    new_moves = []
    move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2),
                    (2, 1), (2, -1)]
    for r_off, c_off in move_offsets:
        nr = r_off + row
        nc = c_off + col
        if 0 <= nr < board_size and 0 <= nc < board_size:
            new_moves.append((nr, nc))
    return new_moves


def pos_to_node_id(row, col, board_size):
    return row * board_size + col


def knight_tour(n, path, u, limit):

    u.color = 'gray'
    path.append(u)
    if n < limit:
        neighbors = ordered_by_avail(u)
        for nbr in neighbors:
            if nbr.color == 'white' and knight_tour(n + 1, path, nbr, limit):
                return True
        else:
            path.pop()
            u.color = 'white'
            return False
    else:
        return True


def ordered_by_avail(u):
    res_list = []
    for v in u.get_neighbors():
        if v.color == 'white':
            c = 0
            for w in v.get_neighbors():
                if w.color == 'white':
                    c += 1
            res_list.append((c, v))
    res_list.sort(key=lambda x: x[0])
    return [y[1] for y in res_list]


bdsize = int(input())
*start_pos, = map(int, input().split())
g = knight_graph(bdsize)
start_vertex = g.get_vertex(pos_to_node_id(*start_pos, bdsize))
if start_vertex is None:
    print("fail")
    exit(0)
    
tour_path = []
done = knight_tour(0, tour_path, start_vertex, bdsize*bdsize - 1)
if done:
    print("success")
else:
    print("fail")

exit(0)