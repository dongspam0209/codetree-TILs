N=int(input())
def func(N):
    if N==1:
        return N
    if N==2:
        return N
    return func(N//3)+func(N-1)

print(func(N))