from heapq import heappop, heappush

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(x1, y1):
    q = [(0, x1, y1)]
    visited = set()
    while q:
        t, x, y = heappop(q)
        if (x, y) in visited:  
            continue
        visited.add((x, y))
        if x == x2 and y == y2:
            return t
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and \
                    ma[nx][ny] != '#' and (nx, ny) not in visited:
                nt = t + abs(int(ma[nx][ny]) - int(ma[x][y]))
                heappush(q, (nt, nx, ny))
    return 'NO'


m, n, p = map(int, input().split())
ma = [list(input().split()) for _ in range(m)]
for _ in range(p):
    x1, y1, x2, y2 = map(int, input().split())
    if ma[x1][y1] == '#' or ma[x2][y2] == '#':
        print('NO')
        continue
    print(bfs(x1, y1))
