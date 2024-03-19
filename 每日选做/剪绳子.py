# 3.19
# 剪绳子 学会了bisect函数
import bisect

n = int(input())
ans = 0
list = [int(i) for i in input().split()]
# list = [int(input()) for _ in range(n)]是错误的
list = sorted(list)
while len(list) != 1:
    t = list.pop(0) + list.pop(0)
    bisect.insort(list, t)
    ans += t
print(ans)
