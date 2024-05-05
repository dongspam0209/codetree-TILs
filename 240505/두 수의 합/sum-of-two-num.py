from collections import defaultdict
n,k=map(int,input().split())
arr=list(map(int,input().split()))
num_dict=defaultdict(list)
for idx,elem in enumerate(arr):
    num_dict[elem].append(idx+1)
cnt=0
for i in num_dict:
    temp_score=k-i
    if temp_score in num_dict:
        cnt+=len(num_dict[temp_score])
print(cnt//2)