m=int(input())
for _ in range(m):
    queue=[]
    stack=[]
    error=False
    n=int(input())
    for _ in range(n):
        operation=input().split()
        if operation[0]=='push':
            queue.append(int(operation[1]))
            stack.append(int(operation[1]))
        elif operation[0]=='pop':
            if queue:
                queue.pop(0)
            else:
                error=True
            if stack:
                stack.pop()
            else:
                error=True
    if error:
        print('error')
        print('error')
    else:
        print(' '.join(map(str,queue)))
        print(' '.join(map(str,stack)))
