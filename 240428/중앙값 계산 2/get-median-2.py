n=int(input())
arr=list(map(int,input().split()))

for idx in range(len(arr)):
    if idx==0:
        temp=arr[0]
        print(temp,end=" ")
    elif idx%2==0:
        temp=arr[0:idx+1]
        temp.sort()
        print(temp[idx//2],end=" ")