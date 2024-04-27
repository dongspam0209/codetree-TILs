a,b,c=map(int,input().split())
def func(n):
    if n<10:
        return n
    return func(n//10)+n%10
print(func(a*b*c))