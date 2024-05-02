import sys
MAX_INT=-sys.maxsize

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))

def calculate_carry(a,b,c):
    calculate_result=[]
    while a>0 or b>0 or c>0:
        position_sum=0
        position_sum=a%10+b%10+c%10
        if position_sum>=10:
            calculate_result.append(-1)
            break
        calculate_result.append(position_sum)
        a//=10
        b//=10
        c//=10
    return calculate_result

sum_list=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a,b,c=arr[i],arr[j],arr[k]
            sum_list.append(calculate_carry(a,b,c))

for ans in sum_list:
    if ans[-1]==-1:
        continue
    max_num=0
    for idx in range(len(ans)):
        max_num+=ans[idx]*10**idx
    MAX_INT=max(max_num,MAX_INT)
    
if MAX_INT<0:
    print(-1)
else:
    print(MAX_INT)