N=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in range(N):
    for j in range(i+1,N):
        partial_sum=0
        if i!=j:
            for k in range(i,j+1):
                partial_sum+=arr[k]
            mean=partial_sum//(j+1-i)
            if mean in arr[i:j+1]:
                cnt+=1
print(cnt)