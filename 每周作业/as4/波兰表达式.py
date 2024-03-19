import operator


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def valuate(postorderexp):
    stack = []
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    for i in postorderexp:
        if is_float(i):
            stack.append(float(i))
        elif i in '+-*/':
            a = stack.pop()
            b = stack.pop()
            stack.append(opers[i](a, b))
    return stack.pop()


exp = input().split()
poexp = reversed(exp)
value = float(valuate(poexp))
print("{:.6f}".format(value))
