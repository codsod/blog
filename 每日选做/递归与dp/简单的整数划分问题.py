sep=[[0]*51 for _ in range(51)]
for j in range(51):
    sep[0][j]=1
for i in range(1,51):
    for j in range(1,51):
        if i<j:
            sep[i][j]=sep[i][i]
        else:
            sep[i][j]=sep[i][j-1]+sep[i-j][j]
    
while True:
    try:
        n=int(input())
        print(sep[n][n])
    except EOFError:
        break