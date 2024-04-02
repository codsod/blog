class unionF:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        xi=self.find(x)
        yi=self.find(y)
        if xi ==yi:
            return
        if self.rank[xi]>self.rank[yi]:
            self.parent[yi]=xi
        elif self.rank[xi]<self.rank[yi]:
            self.parent[xi]=yi
        else:
            self.parent[yi]=xi
            self.rank[xi]+=1
def solve():
    n,m=map(int,input().split())
    uf=unionF(2*n)
    for _ in range(m):
        oper,a,b=input().split()
        a,b=int(a)-1,int(b)-1
        if oper=='D':
            uf.union(a,b+n)
            uf.union(a+n,b)
        else:
            if uf.find(a)==uf.find(b):# or uf.find(a+n)==uf.find(b+n):
                print('In the same gang.')
            elif uf.find(a)==uf.find(b+n) :# or uf.find(a+n)==uf.find(b):
                print('In different gangs.')
            else:
                print('Not sure yet.')


T = int(input())
for _ in range(T):
    solve()
