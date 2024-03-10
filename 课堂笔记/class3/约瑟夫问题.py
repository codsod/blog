# 约瑟夫问题
from collections import deque
def hot_potato(name_list,num):
    queue=deque()
    for name in name_list:
        queue.append(name)

    while len(queue)>1:
        for i in range(num):
            queue.append(queue.popleft())
        queue.popright()
    return queue.popright()

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    monkey=[x for x in range(1,n+1)]
    print(hot_potato(monkey,m))