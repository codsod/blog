import heapq


def dijkstra(graph):
    while path:
        dist, node, fee = heapq.heappop(path)
        if node == N - 1:
            return dist
        for neigh, dis, f in graph[node]:
            ndist = dist + dis
            nfee = fee + f
            if nfee <= K:
                heapq.heappush(path, (ndist, neigh, nfee))
    return -1


K = int(input())
N = int(input())
R = int(input())
graph = [[] for _ in range(N)]
for _ in range(R):
    a, b, c, d = map(int, input().split())
    graph[a - 1].append((b - 1, c, d))
path = [(0, 0, 0)]

res = dijkstra(graph)
print(res)
