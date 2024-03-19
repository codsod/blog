def f(n):
    if n<=2:
        return 1
    if dp[n]!=-1:
        return dp[n];
    else:
        dp[n]=f(n-1)+f(n-2)
        return dp[n]

dp=[-1]*21
n=int(input())
ans=[]
for _ in range(n):
    num=int(input())
    ans.append(str(f(num)))

print('\n'.join(ans))
