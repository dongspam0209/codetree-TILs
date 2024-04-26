N=int(input())
arr=list(map(int,input().split()))
def func(arr):
    for idx in range(len(arr)):
        if arr[idx]%2==0:
            arr[idx]//=2
func(arr)
for idx in arr:
    print(idx,end=" ")