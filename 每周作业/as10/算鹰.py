def dfssearch(row,col):
    matrix[row][col]='-'
    offsets=[(0,1),(0,-1),(1,0),(-1,0)]
    for dx,dy in offsets:
        new_row=row+dx
        new_col=col+dy
        if 0<=new_row<10 and 0<=new_col<10 and matrix[new_row][new_col]=='.':
            dfssearch(new_row,new_col)
            
matrix=[]
num=0
for _ in range(10):
    line=input().strip()
    line=list(line)
    matrix.append(line)
for col in range(10):
    for row in range(10):
        if matrix[row][col]=='.':
            dfssearch(row,col)
            num+=1
print(num)