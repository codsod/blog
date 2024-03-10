calculatelist=input().split()

def calc():
    chr=calculatelist.pop(0)
    if chr in "+-*/":
        return str(eval(calc()+chr+calc()))
    else:
        return chr

print("%.6f" % float(calc()))