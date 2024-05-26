n, m = map(int, input().split())
expenditure = [int(input()) for _ in range(n)]


def check(x):
    num, sum = 1, 0
    for i in range(n):
        if sum + expenditure[i] > x:
            sum = expenditure[i]
            num += 1
        else:
            sum += expenditure[i]
    if num > m:
        return True
    return False


left = max(expenditure)
right = sum(expenditure)
res = 0
while left < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        res = mid
        right = mid
print(res)
