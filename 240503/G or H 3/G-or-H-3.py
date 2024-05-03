import sys
MAX_INT=-sys.maxsize
N,k=map(int,input().split())
arr=['']*10000
for _ in range (N):
    idx,elem=input().split()
    idx=int(idx)-1

    arr[idx]=elem

for i in range(len(arr)-k):
    ans=0
    for j in range(i,i+k+1):
        if arr[j]=='G':
            ans+=1
        elif arr[j]=='H':
            ans+=2
    MAX_INT=max(ans,MAX_INT)

print(MAX_INT)