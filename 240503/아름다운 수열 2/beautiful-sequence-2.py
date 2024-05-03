N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0
for i in range(N-M+1):
    tmp=['']*M
    cnt=0
    for j in range(i,i+M):
        for k in range(M):
            if A[j] == B[k]:
                cnt+=1
                tmp[k]=B[k]
        if cnt==M and '' not in tmp:
            ans+=1

print(ans)