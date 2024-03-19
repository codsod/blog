from collections import defaultdict
from itertools import permutations

a=defaultdict(int)
b=defaultdict(int)
c=defaultdict(int)
d=defaultdict(int)
n=int(input())

for i in input():
    a[i] += 1
  
   
    
     

for i in input():
    
    b[i] += 1
for i in input():
    c[i] += 1
for i in input():
    d[i] += 1

dicts=[a,b,c,d]

def check(word):
    for perms in permutations(dicts,len(word)):
        for i,dic in enumerate(perms):
            if word[i] not in dic:
               break
        else:
            return'YES'
    else:
        return'NO'

for _ in range(n):
    word=input()
    print(check(word))
