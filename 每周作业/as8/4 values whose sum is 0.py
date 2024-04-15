
n=int(input())
matrix=[[0]*4 for _ in range(n)]
answers=[0]
for i in range(n):
    matrix[i]=list(map(int,input().split()))
numzero=0

dictab={}
for i in range(n):
    for j in range(n):
        sumab=matrix[i][0]+matrix[j][1]
        if sumab in dictab:
            dictab[sumab]+=1
        else:
            dictab[sumab]=1
for i in range(n):
    for j in range(n):
        sumcd=matrix[i][2]+matrix[j][3]
        need=-sumcd
        if need in dictab:
            numzero+=dictab[need]
print(numzero)