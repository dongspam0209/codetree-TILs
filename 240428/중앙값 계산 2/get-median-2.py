n=int(input())
arr=list(map(int,input().split()))
arr.sort()
for idx in range(len(arr)):
    if idx%2==0:
        print(arr[idx//2],end=" ")