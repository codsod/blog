N= int (input())
heights=[int(input()) for _ in range(N)]

left=[-1]*N
right=[N]*N

stack=[]
for i in range(N):
    while stack and heights[stack[-1]]<heights[i]:
        stack.pop()
    
    if stack:
        left[i]=stack[-1]
    stack.append(i)

stack=[]

for i in range(N-1,-1,-1):
    while stack and heights[stack[-1]]>heights[i]:
        stack.pop()
    
    if stack:
        right[i]=stack[-1]
    stack.append(i)
    
ans=0
for i in range(N):
    for j in range(left[i]+1,i):
        if right[j]>i:
            ans = max(ans,i-j+1)
            break
print(ans)