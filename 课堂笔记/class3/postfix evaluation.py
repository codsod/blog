def evaluate(postfixexpr):
    nustack=[]

    for index in postfixexpr:
        if index in "+-*/":
            righttoken=nustack.pop()
            lefttoken=nustack.pop()
            nustack.append(str(eval(lefttoken+index+righttoken)))
        else:
            nustack.append(index)
    return float(nustack[0])

n=int(input())
for _ in range(n):
    postfix=input().split()
    print("{:.2f}".format(evaluate(postfix)))
        