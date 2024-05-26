def reverse(s):
    stack=[]
    for char in s:
        if char==')':
            z=[]
            while stack and stack[-1]!='(':
                z.append(stack.pop())
            if stack:
                stack.pop()
            stack.extend(z)
        elif char=='(':
            stack.append(char)
        else:
            stack.append(char)
    return ''.join(stack)

s=input().strip()
print(reverse(s))
