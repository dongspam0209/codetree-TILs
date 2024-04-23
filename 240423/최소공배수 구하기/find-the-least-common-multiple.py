N,M=map(int,input().split())
def Func(N,M):
    i=1
    while True:
        if (N*i)%M==0:
            print(N*i)
            break
        else:
            i+=1

Func(N,M)