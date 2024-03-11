def maxnum(mslist,num,order):
    prev=mslist[order]
    global maxn
    found=False
    if num==0:
        for i in range(len(mslist)):
            found=False
            maxnum(mslist,1,i)
    else:
        for i in range(order+1,len(mslist)):
            cur=mslist[i]
            if cur<=prev:
                found=True
                maxnum(mslist,num+1,i)

    if not found:
        maxn=max(maxn,num)
    

global maxn
missilelist=[]
maxn=0
number_missile=int(input())
missilelist=list(map(int,input().split()))
maxnum(missilelist,0,0)
print(maxn)