n_1,n_2=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
def check(A,B):
    for i in range(0,len(A)-len(B)+1):
        cnt=0
        for j in range(len(B)):
            if B[j]==A[i+j]:
                cnt+=1
        if cnt==len(B):
            print("Yes")
            return
    print("No")
    return

check(A,B)