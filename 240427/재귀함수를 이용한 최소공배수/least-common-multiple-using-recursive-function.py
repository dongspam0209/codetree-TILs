n=int(input())
_arr=list(map(int,input().split()))
def func(n):
    if n==0:
        return _arr[0]
    prev_ans=func(n-1)
    check_num=min(_arr[n],prev_ans)+1
    gcd=0
    for num in range(1,check_num):
        if prev_ans%num==0 and _arr[n]%num==0:
            gcd=num
    return (prev_ans*_arr[n])//gcd

print(func(n-1))