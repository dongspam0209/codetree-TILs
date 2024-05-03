N=int(input())
arr=list(map(int,input().split()))
mean_list=[]
for i in range(N):
    for j in range(i+1,N):
        partial_sum=0
        for k in range(i,j+1):
            partial_sum+=arr[k]
        mean_list.append(partial_sum//(j+1-i))
cnt=0
for case in mean_list:
    if case in arr:
        cnt+=1

print(cnt)