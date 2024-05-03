import sys
n,k=map(int,input().split())
MAX_INT=-sys.maxsize
arr=list(map(int,input().split()))
for i in range(n-k+1):
    max_val=0
    for j in range(i,i+k):
        max_val+=arr[j]
    
    MAX_INT=max(max_val,MAX_INT)

print(MAX_INT)