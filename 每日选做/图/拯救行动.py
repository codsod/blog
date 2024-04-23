import heapq
step = [(0, 1), (0, -1), (1, 0), (-1, 0)]



def save(sx, sy, tmp):
    q=[]
    heapq.heappush(q,(0,sx,sy))
    tmp[sx][sy]=1
    while len(q)!=0:
        time,x,y=heapq.heappop(q)
        for i in range(4):
            nx,ny=x+step[i][0],y+step[i][1]
            if matrix[nx][ny]!=0 and not tmp[nx][ny]:
                if matrix[nx][ny]=='a':
                    return time+1
                elif matrix[nx][ny]=='@':
                    heapq.heappush(q,(time+1,nx,ny))
                    tmp[nx][ny]=1
                elif matrix[nx][ny]=='x':
                    heapq.heappush(q,(time+2,nx,ny))
                    tmp[nx][ny]=1
    return "Impossible"

n = int(input())
for _ in range(n):
    minstep = 2 ** 63 - 1
    N, M = map(int, input().split())
    matrix = [[0 for i in range(M + 2)]]
    tmp=[[0]*(M+2) for _ in range(N+2)]
    for i in range(N):
        line = input().strip()
        row = [0]
        for j in range(M):
            if line[j] == 'r':
                rx, ry = i+1, j+1
            row.append(line[j])
        row.append(0)
        matrix.append(row)
    matrix.append([0 for i in range(M + 2)])
    minstep=save(rx, ry,tmp)
    print(minstep)
