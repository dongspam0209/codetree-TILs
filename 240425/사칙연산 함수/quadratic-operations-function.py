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

print(f'{a} {o} {c} = {func(o,a,c)}')