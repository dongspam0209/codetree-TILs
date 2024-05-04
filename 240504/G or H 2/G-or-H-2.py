import sys
MAX_INT=-sys.maxsize
N=int(input())
arr=['']*100
for _ in range(N):
    idx,word=input().split()
    idx=int(idx)
    arr[idx]=word

for k in range(99):
    for i in range(0,100-k):
        G_cnt=0
        H_cnt=0
        ans=0
        for j in range(i,i+k):
            if arr[j]=='G':
                G_cnt+=1
            elif arr[j]=='H':
                H_cnt+=1
            
        if G_cnt==H_cnt and arr[i]!='' and arr[i+k-1]!='':

            # print('k',k,'시작',i,'끝',i+k-1)
            ans=k-1
            MAX_INT=max(ans,MAX_INT)
        elif H_cnt==0 and arr[i]!='' and arr[i+k-1]!='':

            # print('k',k,'시작',i,'끝',i+k-1)
            ans=k-1
            MAX_INT=max(ans,MAX_INT)
        elif G_cnt==0 and arr[i]!='' and arr[i+k-1]!='':

            # print('k',k,'시작',i,'끝',i+k-1)
            ans=k-1
            MAX_INT=max(ans,MAX_INT)

print(MAX_INT)