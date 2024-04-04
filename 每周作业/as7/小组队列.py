from collections import deque

notequeue = {}
casequeue = []
parent = {}
n = int(input())
datas = []
for _ in range(n):
    line = input().split()
    for data in line:
        parent[data] = _
    datas.append(line)
while True:
    command = input().split()
    if command[0] == 'STOP':
        break
    if command[0] == 'ENQUEUE':
        if parent[command[1]] in casequeue:
            notequeue[parent[command[1]]].append(command[1])
            ins=casequeue.index(parent[command[1]])
            casequeue.insert(ins,command[1])
        else:
            notequeue[parent[command[1]]] = deque([command[1]])
            casequeue.insert(0,parent[command[1]])
    if command[0] == 'DEQUEUE':
        first = next(iter(notequeue.items()))
        print(notequeue[first[0]].popleft())
        if len(notequeue[first[0]])==0:
            del notequeue[first[0]]
        casequeue.pop()