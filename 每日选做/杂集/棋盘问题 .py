while True:
    n, k = map(int, input().split())
    if n == -1 and k == -1:
        break
    keynum = 0
    son = 1
    keyboard = [[0] * n for i in range(n)]
    for _ in range(n):
        line = input()
        for i in range(n):
            if line[i] == '#':
                keyboard[_][i] = 1
                keynum += 1
    for i in range(k):
        son = son * (keynum - i) / (i + 1)
    print(int(son))
