import sys
MIN_INT=sys.maxsize
N,H,T=map(int,input().split()) #H height over T times
arr=list(map(int,input().split()))
for i in range(N-T+1):
    cost=0
    for j in range(i,i+T): #kernel move
        cost+=abs(arr[j]-H)
        # print(arr[j],end=" ")
    # print()
    # print('i:',i,'cost:',cost)
    MIN_INT=min(MIN_INT,cost)
print(MIN_INT)