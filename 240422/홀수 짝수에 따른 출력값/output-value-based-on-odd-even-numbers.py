N=int(input())
def func(N):
    if N==1 or N==2:
        return N
    return func(N-2)+N

print(func(N))