def orderToPost(inexp):
    postorder = []
    opStack = []
    pres = {'+': 1, '-': 1, '*': 2, '/': 2}
    number = ''
    for i in inexp:
        if i.isnumeric() or i == '.':
            number += i
        else:
            if number:
                number = float(number) if '.' in number else int(number)
                postorder.append(number)
                number = ''
            if i in pres:
                while opStack and opStack[-1] in pres and pres[i] <= pres[
                        opStack[-1]]:
                    postorder.append(opStack.pop())
                opStack.append(i)
            elif i == '(':
                opStack.append(i)
            elif i == ')':
                while opStack[-1] != '(':
                    postorder.append(opStack.pop())
                opStack.pop()
    if number:
        number = float(number) if '.' in number else int(number)
        postorder.append(number)

    while opStack:
        postorder.append(opStack.pop())

    return ' '.join(str(i) for i in postorder)


n = int(input())
for _ in range(n):
    infix = input()
    print(orderToPost(infix))
