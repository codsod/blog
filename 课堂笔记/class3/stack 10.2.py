def operator(dec_num,base):
    digits="0123456789ABCDEF"
    s=[]
    expression=""
    while dec_num:
        decc=dec_num%base
        s.append(digits[decc])
        dec_num=dec_num//base
    while s:
        expression=expression+str(s.pop())
    return expression

print(operator(int(input()),8))