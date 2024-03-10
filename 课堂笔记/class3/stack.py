lines=[]
while True:
    try:
        lines.append(input())
    except EOFError:
        break

for a in lines:
    stack=[]
    mark=[]
    for index in range(len(a)):
        if a[index]=='(':
            stack.append(index)
            mark+=' '
        elif a[index]==')':
            if not stack:
                mark+='?'
            else:
                mark+=' '
                stack.pop()
        else:
            mark+=' '
    while len(stack):
        mark[stack.pop()]='$'

    print(a)
    print(''.join(map(str,mark)))