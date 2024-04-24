n,m=map(int,input().split())
def func(n,m):
    for num in range(max(n,m),1,-1):
        if m==1 or n==1:
            print(m)
            return
            
        if m%num==0 and n%num==0:
            print(num)
            return

func(n,m)