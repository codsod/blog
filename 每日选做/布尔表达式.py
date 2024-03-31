# http://cs101.openjudge.cn/2024sp_routine/06263/
def postfix(s):
    stack = []
    order = []
    for char in s:
        if char in ['V', 'F']:
            order.append(char)
            if stack and stack[-1] == '!':
                order.append(stack.pop())
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                order.append(stack.pop())
            stack.pop()
        elif char in [ '&', '|']:
            while stack and stack[-1] in ['!', '&', '|']:
                order.append(stack.pop())
            stack.append(char)
        elif char =='!':
            stack.append(char)
    while stack:
        order.append(stack.pop())
    return order
def boolexp(post):
    stack=[]
    for char in post:
        if char == 'V':
            stack.append(True)
        elif char=='F':
            stack.append(False)
        elif char == '!':
            stack.append(not stack.pop())
        else:
            a=stack.pop()
            b=stack.pop()
            if char == '&':
                stack.append(a and b)
            else:
                stack.append(a or b)
    return 'V' if stack[0] else 'F'


def spli(s):
    if ' ' in s:
        a = ''
        for char in s:
            if char != ' ':
                a += char
        s = a
    return s


while True:
    try:
        s = input().strip()
        s = spli(s)
        post = postfix(s)
        print(boolexp(post))

    except EOFError:
        break
