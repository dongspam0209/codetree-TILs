M,D=map(int,input().split())
def func(M,D):
    if M>12:
        print("No")
        return
    else:
        day_arr=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        if day_arr[M]<D:
            print("No")
        else:
            print("Yes")

func(M,D)