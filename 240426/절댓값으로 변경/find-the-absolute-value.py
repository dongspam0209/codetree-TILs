N=int(input())
arr=list(map(int,input().split()))
def func(arr):
    for idx in range(N):
        arr[idx]=abs(arr[idx])
func(arr)
for num in arr:
    print(num,end=" ")