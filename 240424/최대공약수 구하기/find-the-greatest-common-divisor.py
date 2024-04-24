n,m=map(int,input().split())
def func(n,m):
    for num in range(max(n,m),1,-1):

        if m%num==0 and n%num==0:
            print(num)
            return
        
        if num==1:
            print(num)


func(n,m)