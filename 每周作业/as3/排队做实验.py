n=int(input())
timelist=list(map(int,input().split()))
indexlist=sorted(range(1,n+1),key=lambda x:timelist[x-1])
timelist.sort()
total=sum((n-i-1)*timelist[i] for i in range(n))/n

for i in range(n):
    print(indexlist[i],end=" ")
print()
print("{:.2f}".format(total))