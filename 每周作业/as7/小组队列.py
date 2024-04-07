from collections import deque

n = int(input())
parent = {}
for _ in range(n):
    line = input().split()
    for data in line:
        parent[data] = _
queue = deque()
havebe = {i: deque() for i in range(n)}

while True:
    line = input().split()
    if line[0] == 'STOP':
        break
    elif line[0] == 'ENQUEUE':
        data = line[1]
        havebe[parent[data]].append(data)
        if parent[data] not in queue:
            queue.append(parent[data])
    elif line[0] == 'DEQUEUE':
        group = queue[0]
        print(havebe[group].popleft())
        if not havebe[group]:
            queue.popleft()
