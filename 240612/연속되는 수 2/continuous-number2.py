import sys

MAX_INT=-sys.maxsize
N=int(input())
arr=[]
for _ in range(N):
    arr.append(int(input()))

count=1
for i in range(N-1):
    if arr[i]==arr[i+1]:
        count+=1
    else:
        MAX_INT=max(count,MAX_INT)
        count=1
print(MAX_INT)