def Hanoi(n,origin,translation,destination):
    orderlist=[]
    if n==1:
        a="1:{}->{}".format(origin,destination)
        orderlist.append(a)
        return orderlist
    orderlist+=Hanoi(n-1,origin,destination,translation)
    orderlist.append("{}:{}->{}".format(n,origin,destination))
    orderlist+=Hanoi(n-1,translation,origin,destination)
    return orderlist

n,a,b,c=map(str,input().split())
n=int(n)
movelist=Hanoi(n,a,b,c)
for i in movelist:
    print(i)
    

