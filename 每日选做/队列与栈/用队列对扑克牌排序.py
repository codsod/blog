from collections import deque

order = deque()
queuesdict = {}
for i in range(1, 10):
    queuesdict[i] = deque()
queuesdict["A"] = deque()
queuesdict["B"] = deque()
queuesdict["C"] = deque()
queuesdict["D"] = deque()
n = int(input())
s = input().split()
for char in s:
    number = int(char[1])
    queuesdict[number].append(char)
for i in range(1, 10):
    print(f"Queue{i}:", end="")
    print(*queuesdict[i], sep=" ")
    for j in queuesdict[i]:
        queuesdict[j[0]].append(j)
for i in ["A", "B", "C", "D"]:
    print(f"Queue{i}:", end="")
    print(*queuesdict[i], sep=" ")
    order.extend(queuesdict[i])
print(*order, sep=" ")