n=int(input())
lst=list(map(int,input().split()))
stack=[]

for i in range(len(lst)):
	while stack and lst[stack[-1]]<lst[i]:
		lst[stack.pop()]=str(i+1)
	stack.append(i)
while stack:
	lst[stack.pop()]='0'
print(' '.join(lst))#实际操作中，可以再单独开一个数组存放结果，以避免数据覆盖
a=6.52
print(f'一位小数 {a:.1f}')