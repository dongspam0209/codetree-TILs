import sys
MIN_INT=sys.maxsize
N,S=map(int,input().split())
arr=list(map(int,input().split()))
check=[]
for i in range(N):
    for j in range(i+1,N): #i,j is gonna be deleted index
        sum=0
        for k in range(N):
            if k==i or k==j:
                continue
            sum+=arr[k]
        gap=abs(S-sum)
        MIN_INT=min(MIN_INT,gap)
print(MIN_INT)