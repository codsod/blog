def is_stackout_reasonable(init,post):
    if len(init)!=len(post):
        return 'NO'
    postindex=0
    stack=[]
    for i in init:
        stack.append(i)
        if i==post[postindex]:
            postindex+=1
            stack.pop()
        while stack and stack[-1]==post[postindex]:
            stack.pop()
            postindex+=1
    while stack:
        if stack[-1]==post[postindex]:
            stack.pop()
            postindex+=1
        else:
            return 'NO'
    return 'YES'

init=input()
while True:
    try:
        post=input()
        print(is_stackout_reasonable(init,post))
    except EOFError:
        break
    