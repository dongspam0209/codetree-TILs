import sys
MAX_INT=-sys.maxsize

N,K=map(int,input().split())
arr=[0]*101 # basket position
for _ in range(N):
    amount,idx=map(int,input().split())
    arr[idx]+=amount

if 2*K>=100:
    print(sum(arr))
    exit()
    
for i in range(100-2*K+1):
    temp_sum=0
    for j in range(i,i+2*K+1):
        temp_sum+=arr[j]
    print(temp_sum)
    MAX_INT=max(temp_sum,MAX_INT)


print(MAX_INT)