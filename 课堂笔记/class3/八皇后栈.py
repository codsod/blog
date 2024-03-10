def queen_stack(n):
    stack=[]# 保存状态的栈
    solutions=[]

    stack.append((0,[]))
    while stack:
        row,cols=stack.pop()
        if row==n:
            solutions.append(cols)
        else:
            for col in range(n):
                if is_valid(row,col,cols):
                    stack.append((row+1,cols+[col]))
    return solutions

def is_valid(row,col,cols):
    for r in range(row):
        if cols[r]==col or abs(row-r)==abs(col-cols[r]):
            return False
    return True

def get_queen_string(b):
    solutions=queen_stack(8)
    if b>len(solutions):
        return None
    b=len(solutions)+1-b
    queen_string=''.join(str(col+1) for col in solutions[b-1])
    return queen_string

test_cases = int(input())  
for _ in range(test_cases):
    b = int(input()) 
    queen_string = get_queen_string(b)
    print(queen_string)