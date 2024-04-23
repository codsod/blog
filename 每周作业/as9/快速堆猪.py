stack = []
mins = []
while True:
    try:
        r = input().split()
        if r[0] == 'pop':
            if stack:
                stack.pop()
                if mins:
                    mins.pop()
        elif r[0] == 'push':
            tar = int(r[1])
            stack.append(tar)
            if not mins:
                mins.append(tar)
            else:
                h = mins[-1]
                mins.append(min(h, tar))
            # 由于栈的顺序性，辅助站中只需要记住到他为止最小的元素即可
        elif r[0] == 'min':
            if mins:
                print(mins[-1])
    except EOFError:
        break
