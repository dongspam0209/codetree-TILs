N=int(input())
def func(n):
    arr=[1,2,3,4,5,6,7,8,9]
    for i in range(n):
        for j in range(n):
            idx=(i*n+j)%9
            print(arr[idx],end=" ")
        print()


func(N)