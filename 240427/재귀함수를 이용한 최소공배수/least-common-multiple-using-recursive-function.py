n=int(input())
_arr=list(map(int,input().split()))
def func(n):
    if n==0:
        return _arr[0]
    
    return lcm(func(n-1),_arr[n])

def lcm(a,b):
    gcd=1
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    
    return (a*b)//gcd

print(func(n-1))