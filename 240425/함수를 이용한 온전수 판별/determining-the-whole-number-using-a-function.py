a,b=map(int,input().split())
def func(a,b):
    cnt=0
    for num in range(a,b+1):
        if num%2!=0 and num%10!=5 and (num%3!=0 or num%9==0):
            cnt+=1

    return cnt

print(func(a,b))