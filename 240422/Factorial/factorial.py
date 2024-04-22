N=int(input())
def factorial(N):
    if N==1:
        return N
    return factorial(N-1)*N

print(factorial(N))