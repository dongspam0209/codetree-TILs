a,b=map(int,input().split())
def func(a,b):
    ans=0
    if a==b:
        return ans
    for num in range(a,b+1):
        is_prime=True
        for idx in range(2,num):
            if num%idx==0:
                is_prime=False
        
        if is_prime:
            ans+=num

    return ans

print(func(a,b))