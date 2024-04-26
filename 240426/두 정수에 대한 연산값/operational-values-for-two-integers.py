a,b=map(int,input().split())
def func(a,b):
    if a>b:
        a+=25
        b*=2
    else:
        a*=2
        b+=25
    return a,b
c,d=func(a,b)
print(c,d)