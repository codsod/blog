class Node:
    def __init__(self, id=0):
        self.id=id
        self.next={}
def add(root, nums):
    node=root
    l=len(nums)
    samen=0
    for k in nums:
        if k in node.next.keys():
            samen += 1
        if k not in node.next.keys():
            node.next[k]=Node(k)
        node=node.next[k]
    if l==samen: return False
    return True
datan=int(input())
for _ in range(datan):
    n=int(input())
    Tree=Node()
    numlist=[]
    for _ in range(n):
        numlist.append(str(input()))
    numlist.sort(reverse=True)
    for num in numlist:
        if not add(Tree,num):
            print("NO")
            break
    else:
        print("YES")
