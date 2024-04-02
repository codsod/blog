#超时代码
#elif a[0] == c[0] and b[0] != c[0]:
#       return zipper(a[1:], b, c[1:])
#   elif b[0] == c[0] and a[0] != c[0]:
#       return zipper(a, b[1:], c[1:])
#   elif a[0] == b[0] and a[0] == c[0]:
#       x = zipper(a[1:], b, c[1:])
#       y = zipper(a, b[1:], c[1:])
#       return x or y
#   elif a[0] != c[0] and b[0] != c[0]:
#        return False
#超时代码
#elif a[0] == c[0] and b[0] != c[0]:
#       return zipper(a[1:], b, c[1:])
#   elif b[0] == c[0] and a[0] != c[0]:
#       return zipper(a, b[1:], c[1:])
#   elif a[0] == b[0] and a[0] == c[0]:
#       x = zipper(a[1:], b, c[1:])
#       y = zipper(a, b[1:], c[1:])
#       return x or y
#   elif a[0] != c[0] and b[0] != c[0]:
#        return False
def zipper(a, b, c):
    if a == '0' and b == '0':
        return True
    if a[-1] == c[-1]:
        if zipper(a[:len(a) - 1], b, c[:len(c) - 1]):
            return True
    if b[-1] == c[-1]:
        if zipper(a, b[:len(b) - 1], c[:len(c) - 1]):
            return True
    return False


n = int(input())
datan = 0
for _ in range(n):
    datan += 1
    a, b, c = input().split()
    a = '0' + a
    b = '0' + b
    res = 'yes' if zipper(a, b, c) else 'no'
    print(f'Data set {datan}: {res}')

def dfs(x,y):
    if y == -1 and x == -1:
        return True
    if x>= 0 and a[x] == c[x+y+1]:
        if dfs(x-1,y):
            return True
    if y >= 0 and b[y]== c[x+y+1]:
        if dfs(x,y-1):
            return True
        return False
for p in range(int(input())):
    a,b,c = input().split()
    if dfs(len(a)-1,len(b)-1):
        print(f'Data set {p+1}: yes')
    else:
        print(f'Data set {p+1}: no')
