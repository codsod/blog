from collections import deque
n,m=map(int,input().split())
queue=deque([-1]*n)
cases=0
search=input().split()
for i in search:
    if i not in queue:
        cases+=1
        queue.appendleft(i)
        queue.pop()
print(cases)