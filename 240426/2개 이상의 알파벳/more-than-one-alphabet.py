A=input()
def func(A):
    unique=set(A)
    if len(unique)>=2:
        print("Yes")
    else:
        print("No")
func(A)