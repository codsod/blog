datanum = {}
n, k = map(int, input().split())
line = list(map(int, input().split()))
line.sort()
for i in line:
    datanum[i] = datanum[i] + 1 if i in datanum else 1
casenum = 0
if k == 0:
    print(1 if line[0] > 1 else -1)
elif k == n:
    print(line[-1])
else:
    for num, cases in datanum.items():
        casenum += cases
        datanum[num] = casenum
        if casenum < k:
            continue
        elif casenum == k:
            print(num)
            break
        else:
            print(-1)
            break
