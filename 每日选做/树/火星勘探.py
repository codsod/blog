from collections import defaultdict
def preorderfit(numl):
    stack=[]
    sons=defaultdict(int)
    if numl[0]!='#':
        stack.append(numl[0])
    for i in range(1,len(numl)):
        if stack:
            sons[stack[-1]]+=1
            if sons[stack[-1]]==2:
                stack.pop()
            if numl[i]!='#':
                stack.append(i)
        else:
            return False
    if  stack:
        return False
    return True
            
while True:
    num=int(input())
    if num == 0:
        break
    ptr=0
    numl=list(input().split())
    if len(numl)!=num:
        ptr=0
    else:
        if preorderfit(numl):
            ptr=1
        else:
            ptr=0
    print('T' if ptr==1 else 'F')