N=int(input())
def fibonacci(N):
    if N==0 or N==1:
        return N

    return fibonacci(N-1)+fibonacci(N-2)

print(fibonacci(N))