import heapq

sx,sy=map(int,input().split())
ex,ey=map(int,input().split())
m=int(input())
blocks=set()
for _ in range(m):
    block=tuple(map(int,input().split()))
    blocks.add(block)

DIR=8
rx,ry=[1,-1,2,2,1,-1,-2,-2],[2,2,1,-1,-2,-2,-1,1]
bx,by=[0,1,0,-1],[1,0,-1,0]

queue=[(0,sx,sy,f'({sx},{sy})')]
ans=0
shortdist=float('inf')
onlypath=''

while queue:
    dist,x,y,path=heapq.heappop(queue)
    if dist>shortdist:
        break
    if x==ex and y==ey:
        ans+=1
        if ans==1:
            onlypath=path
            shortdist=dist
    
    for i in range(DIR):
        nx,ny=x+rx[i],y+ry[i]
        dx,dy=x+bx[i//2],y+by[i//2]
        if (dx,dy) not in blocks:
            queue.append((dist+1,nx,ny,path+f'-({nx},{ny})'))

print(onlypath if ans==1 else ans)
