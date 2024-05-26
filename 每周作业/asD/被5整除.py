def erjin(s):
    n=len(s)
    sum=0
    pos=0
    while s:
        num = s.pop()
        sum+=num*(2**pos)
        pos+=1
    if sum%5==0:
        return True
    else:
        return False
c=list(input())
a=[int(i) for i in c]
b=[]
for i in range(len(a)):
    if erjin(a[:i+1]):
        b.append(1)
    else:
        b.append(0)
for i in b:
    print(i,end='')
