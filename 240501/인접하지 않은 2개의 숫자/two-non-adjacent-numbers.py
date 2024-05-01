import sys
MAX_INT=-sys.maxsize
n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    for j in range(len(arr)):
        if i==j or i==j+1 or i==j-1:
            continue
        else:
            MAX_INT=max(MAX_INT,(arr[i]+arr[j]))
print(MAX_INT)