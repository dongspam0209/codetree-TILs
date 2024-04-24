# N,M=map(int,input().split())
# def Func(N,M):
#     i=1
#     while True:
#         if (N*i)%M==0:
#             print(N*i)
#             break
#         else:
#             i+=1

# Func(N,M)

N,M=map(int,input().split())

def Fun(N,M):
    ans=0
    for num in range(1,min(N,M)):
        if N%num==0 and M%num==0:
            ans=num
    print((N*M)//ans)


Fun(N,M)