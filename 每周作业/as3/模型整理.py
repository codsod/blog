n=int(input())
dic={}
for i in range(n):
    name,date=input().split("-")
    if name not in dic:
        dic[name]=[]
    if date[-1]=="M":
        order=float(float(date[:-1])/1000)
    else:
        order=float(date[:-1])
    dic[name].append((date,order))

di=sorted(dic)
for key in di:
    valueorder=sorted(dic[key],key=lambda x:x[-1])
    valuelist=[x[0] for x in valueorder]
    value=', '.join(valuelist)
    print("{}: {}".format(key,value))
    