N=int(input())
def _print(N):
    tmp=0
    for idx in range(N+1):
        tmp+=idx
    
    return tmp//10

print(_print(N))