def infixtopostfix(infixexpr):
    precedence={}
    precedence['(']=1
    precedence['*']=3
    precedence['/']=3
    precedence['+']=2
    precedence['-']=2
    opstack=[]
    postfix=[]
    number=''

    for token in infixexpr:
        if token.isnumeric() or token=='.':
            number=number+token
        else:
            if number:
                num=float(number)
                postfix.append(int(num) if num.is_integer() else num)
                number=''
            if token=='(':
                opstack.append(token)
            elif token==')':
                topstack=opstack.pop()
                while topstack!='(':
                    postfix.append(topstack)
                    topstack=opstack.pop()
            else:
                while opstack and precedence[opstack[-1]]>=precedence[token]:
                    postfix.append(opstack.pop())
                opstack.append(token)
    if number:
        num=float(number)
        postfix.append(int(num) if num.is_integer() else num)
    while opstack:
            postfix.append(opstack.pop())
    return " ".join(str(x) for x in postfix)

n=int(input())
for _ in range(n):
    print(infixtopostfix(input()))
