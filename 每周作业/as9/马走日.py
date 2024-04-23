dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

ans = 0


def solve(x, y, t, d):
    if t == d:
        global ans
        ans += 1
        return
    for ind in range(8):
        nx = x + dx[ind]
        ny = y + dy[ind]
        if 0 <= nx < n and 0 <= ny < m and martix[nx][ny] == 0:
            martix[nx][ny] = 1
            solve(nx, ny, t, d + 1)
            martix[nx][ny] = 0


n = int(input())
for _ in range(n):
    n, m, x, y = map(int, input().split())
    martix = [[0] * m for _ in range(n)]
    ans = 0
    martix[x][y] = 1
    solve(x, y, n * m, 1)
    print(ans)
