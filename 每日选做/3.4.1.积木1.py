from collections import defaultdict
from itertools import permutations

a = defaultdict(int)
b = defaultdict(int)
c = defaultdict(int)
d = defaultdict(int)
n = int(input())

for i in input():
    a[i] += 1
for i in input():
    b[i] += 1
for i in input():
    c[i] += 1
for i in input():
    d[i] += 1

listl = [a, b, c, d]


def check(word):
    for perms in permutations(listl, len(word)):
        for i, key in enumerate(perms):
            if word[i] not in key:
                break
        else:
            return 'YES'
    else:
        return 'NO'


for _ in range(n):
    word = input()
    print(check(word))
