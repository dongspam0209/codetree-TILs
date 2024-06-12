import sys

MAX_INT=-sys.maxsize
N=int(input())
arr=[]
for _ in range(N):
    arr.append(int(input()))

count=0
for i in range(N):

    if i==0 or arr[i]==arr[i-1]:
        count+=1
        MAX_INT=max(MAX_INT,count)
    else:
        count=1
print(MAX_INT)