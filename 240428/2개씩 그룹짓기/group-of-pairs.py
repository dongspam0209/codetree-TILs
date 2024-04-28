N=int(input())
arr=list(map(int,input().split()))
arr.sort()
ans_list=[]
for idx in range(len(arr)//2):
    first,last=arr[idx],arr[-(idx+1)]
    ans_list.append(first+last)

print(max(ans_list))