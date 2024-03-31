# 拿到题最容易想到的思路是双指针，从母序列从头找到尾，如果子序列也结束了，那么则yes，否则no
#  不过窥看其本质，实际上是子序列中的每个字母要按顺序出现在母序列中，所以我们可以直接使用index函数，
# 在母序列按顺序一个一个找子序列中的元素。注意：这里的“按顺序”就体现在，每在母序列找到一个元素，
# 就在这个元素的下一位开始找，也就是要进行切片操作
def a(s,t):
    start=0
    s=list(reversed(s))
    while s:
        try:
            p=s.pop()
            nt=t[start:]
            newstart=nt.index(p)+1
            start+=newstart
        except ValueError:
            return 'No'
    return 'Yes'
            
    
while True:
    try:
        s,t=map(str,input().split())
        print(a(s,t))
    except EOFError:
        break