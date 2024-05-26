import heapq

datan=int(input())
for _ in range(datan):
    data=[]
    jinum=0
    left=[]
    right=[]
    medians=[]
    line=list(map(int,input().split()))
    middle=line[0]
    for i in line:
        if i>=middle:
            if len(right)-len(left)==1:
                heapq.heappush(left,-heapq.heappop(right))
            heapq.heappush(right,i)
        elif i<middle:
            if len(right)==len(left):
                heapq.heappush(right,-heapq.heappop(left))
            heapq.heappush(left,-i)
        if len(right)==len(left):
            middle=-left[0]
        else:
            middle=right[0]
        le=len(left)+len(right)
        if le%2==1:
            jinum+=1
            medians.append(middle)
    print(jinum)
    print(*medians)

