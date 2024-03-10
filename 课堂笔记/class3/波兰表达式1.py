global calculatelist
global pos
calculatelist=[]
pos=-1

def EXp():
    global pos
    pos+=1
    char=calculatelist[pos]
    if char=='+':
        return EXp()+EXp()
    if char=='-':
        return EXp()-EXp()
    if char=='*':
        return EXp()*EXp()
    if char=='/':
        return EXp()/EXp()
    else:
        return float(char)

calculatelist=list(input().split())
print("{:.6f}".format(EXp()))
    
    