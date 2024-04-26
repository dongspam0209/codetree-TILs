n,m=map(int,input().split())
A=[0]
A.extend(list(map(int,input().split())))

def func():
    sum=0
    global m
    
    while m>=1:
        # print(f'm:{m}')
        sum+=A[m]

        if m%2==1:
            m-=1
        else:
            m//=2

        # print(sum)
    
    return sum

ans=func()
print(ans)