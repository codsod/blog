calculatelist=input().split()
calculatelist.reverse()
stack=[]

while  calculatelist:
    a=calculatelist.pop(0)
    if a in "+-*/":
        c=float(stack.pop())
        
        stack.append(str(eval(f"c{a}d")))
    else:
        stack.append(a)

print("{:.6f}".format(float(stack[0])))
