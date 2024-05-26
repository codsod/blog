import sys
from heapq import heappop,heappush
def prim(n,st):
    queue = [0]
    edge=[]
    min = 0
    while len(queue)<n:
        tmp=queue[-1]
        for i in range(n):
            if i in queue:
                continue
            heappush(edge,(matrix[tmp][i],tmp,i))
        ddist,tmp1,new=heappop(edge)
        while new in queue:
            ddist,tmp1,new=heappop(edge)
        queue.append(new)
        min+=ddist




    return min

while True:
    try:
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        distance = sys.maxsize
        distance=prim(n,0)
        print(distance)
    except EOFError:
        break
        

