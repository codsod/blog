def medvalue(list):
    list.sort()
    if len(list)%2==1:
        ins=int((len(list)-1)/2)
        meddist=list[ins]
    else:
        med=int(len(list)/2)
        meddist=(list[med-1]+list[med])/2
    return meddist

n=int(input())
xypairs=[i[1:-1] for i in input().split()]
distance=[sum(map(int,i.split(","))) for i in xypairs]
*money,=map(int,input().split())
value=[float(distance[i]/money[i]) for i in range(n)]
medval=medvalue(value.copy())
medmon=medvalue(money.copy())
t=0
for i in range(n):
    if value[i]>medval and money[i]<medmon:
        t+=1
print(t)