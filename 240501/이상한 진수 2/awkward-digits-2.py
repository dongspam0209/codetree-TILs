import sys
MAX_INT=-sys.maxsize
a=list(map(int,input()))
ans=[]
for idx in range(len(a)):
    temp=[0]*len(a)
    if a[idx]==0:
        temp[idx]=1
        temp[0:idx]=a[0:idx]
        temp[idx+1:len(a)]=a[idx+1:len(a)]
    else:
        temp[idx]=0
        temp[0:idx]=a[0:idx]
        temp[idx+1:len(a)]=a[idx+1:len(a)]
    ans.append(temp)

# print(ans)
for sampled_ans in ans:
    temp=sampled_ans[::-1]
    decimal=0
    for idx in range(len(temp)):
        decimal+=temp[idx]*2**idx
    MAX_INT=max(decimal,MAX_INT)

print(MAX_INT)