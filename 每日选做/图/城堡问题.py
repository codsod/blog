D = [(0, -1), (-1, 0), (0, 1), (1, 0)]
Max=0


def mapcount(i, j, visited):
    coter=1
    visited[i][j] = 1
    d = []
    value = int(map[i][j])
    zhuan = {8: 3, 4: 2, 2: 1, 1: 0}
    N = 8
    while N > 0:
        if value // N == 1:
            value -= N
        else:
            d.append(D[zhuan[N]])
        N = N // 2
    for dx, dy in d:
        if not visited[i + dx][j + dy]:
            coter+=mapcount(i + dx, j + dy, visited)
    return coter


x, y = int(input()), int(input())
map = [input().split() for _ in range(x)]
visited = [[0] * y for _ in range(x)]
counter = 0
for i in range(x):
    for j in range(y):
        if not visited[i][j]:
            Max=max(Max,mapcount(i, j, visited))
            counter += 1
print(counter)
print(Max)
