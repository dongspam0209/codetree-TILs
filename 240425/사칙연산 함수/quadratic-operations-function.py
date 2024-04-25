a,o,c=input().split()
a=int(a)
c=int(c)
def func(character,a,b):
    if character=='+':
        return a+b
    elif character=='-':
        return a-b
    elif character=='/':
        return a//b
    elif character=='*':
        return a*b
    else:
        return False

ans=func(o,a,c)
if ans==False:
    print("False")
else:
    print(f'{a} {o} {c} = {ans}')