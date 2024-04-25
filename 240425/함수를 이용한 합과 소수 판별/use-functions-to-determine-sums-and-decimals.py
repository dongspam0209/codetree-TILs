a,b=map(int,input().split())
def func(a,b):
    cnt=0
    for num in range(a,b+1):
        prime_numcheck=True
        for check in range(2,num):
            if num%check==0:
                prime_numcheck=False
        if prime_numcheck:
            check_number_even=check_even(num)
            if check_number_even%2==0:
                cnt+=1

    return cnt

def check_even(a):
    ans=0
    while a>=10:
        temp=a%10
        a//=10
        ans+=temp
    ans+=a
    return ans

print(func(a,b))