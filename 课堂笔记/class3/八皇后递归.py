def solve_n_queens(n):
    solutions=[]
    queens=[-1]*n

    def backtrack(row):
        if row==n:
            solutions.append(queens.copy())
        else:
            for col in range(n):
                if is_valid(row,col):
                    queens[row]=col
                    backtrack(row+1)
                    queens[row]=-1
    
    def is_valid(row,col):
        for r in range(row):
            if queens[r]==col or abs(row-r)==abs(col-queens[r]):
                return False
        return True
    
    backtrack(0)
    return solutions

def get_queen_string(b):
    solutions=solve_n_queens(8)
    if b>len(solutions):
        return None
    queen_string=''.join(str(col+1) for col in solutions[b-1])
    return queen_string

cases=int(input())
for _ in range(cases):
    b=int(input())
    queen_string=get_queen_string(b)
    print(queen_string)
