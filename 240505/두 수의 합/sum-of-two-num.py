n,k=map(int,input().split())
arr=list(map(int,input().split()))
num_dict={}
for idx,elem in enumerate(arr):
    num_dict[idx]=elem

cnt=0
for i in range(n-1):
    for j in range(i+1,n):
        if num_dict[i]+num_dict[j]==k:
            cnt+=1
print(cnt)