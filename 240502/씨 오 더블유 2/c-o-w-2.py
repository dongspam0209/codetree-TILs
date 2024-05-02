N=int(input())
arr=input()
cnt=0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if arr[i]=='C' and arr[j]=='O' and arr[k]=='W':
                cnt+=1

print(cnt)