# 仔细思考可以发现其实有向无环图的最大边数是关于节点个数的函数，所以只需要计算出已提供的边数（注意要减去重复的边，这也是为什么要字典里面套集合的原因），再相减即可

from collections import defaultdict
n,m=map(int,input().split())
dict=defaultdict(set)
for _ in range(m):
    a,b=map(int,input().split())
    dict[a].add(b)
edgenum=0
for key in dict:
    edgenum+=len(dict[key])
addedge=n*(n-1)/2-edgenum
print(int(addedge))