n,m=map(int,input().split())
def func(n,m):
    for num in range(max(n,m),0,-1):
        # print(num)
        if m%num==0 and n%num==0:
            print(num)
            return
        
        if num==1:
            print(num)
            return


func(n,m)