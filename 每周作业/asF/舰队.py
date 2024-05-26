def dfs(node, color):
    color[node] = 1
    for neigh in neighs[node]:
        if color[neigh] == 1:
            return True
        if color[neigh] == 0 and dfs(neigh, color):
            return True
    color[node] = 2
    return False


datas = int(input())
for _ in range(datas):
    n, m = map(int, input().split())
    neighs = [[] for _ in range(n)]
    flag = False
    for _ in range(m):
        x, y = map(int, input().split())
        neighs[x - 1].append(y - 1)
    color = [0] * n
    for i in range(n):
        if color[i] == 0:
            if dfs(i, color):
                flag = True
                break
    print('Yes' if flag else 'No')
