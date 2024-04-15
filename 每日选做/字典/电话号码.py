from collections import defaultdict

N = int(input())
for _ in range(N):
    ptr = 0
    phonenumber = defaultdict(int)
    datan = int(input())
    data = []
    for _ in range(datan):
        line = input()
        phonenumber[line] = 1
        data.append(line)
    for _ in data:
        NO = ''
        for i in _:
            NO += i
            if phonenumber[NO] != 0 :
                phonenumber[NO] += 1
                if phonenumber[NO]>2:
                    ptr=1
                    break
    if ptr == 1:
        print('NO')
    else:
        print('YES')
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346