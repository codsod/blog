answer=[]

def dfs(s):
    for col in range(1,9):
        for i in range(len(s)):
            if str(col)==s[i] or \
            abs(col-int(s[i]))==abs(len(s)-i):
                break
        else:
            if len(s)==7:
                answer.append(s+str(col))
            else:
                dfs(s+str(col))
dfs('')

n = int(input())
for _ in range(n):
    a=int(input())
    print(answer[a-1])