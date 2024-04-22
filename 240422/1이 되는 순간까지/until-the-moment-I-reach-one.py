N=int(input())
case=list()

def func(N):
    if N==1:
        return
    a=N%2
    
    if a==0:#짝수
        func(N//2)
        case.append('*')
    if a==1:
        func(N//3)
        case.append('*')
        
    return case



ans=func(N)
print(len(ans))