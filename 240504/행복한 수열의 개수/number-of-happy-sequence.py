n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
ans=0
for i in range(n):
    cnt=1
    for j in range(n-1):
        cur,nex=arr[i][j],arr[i][j+1]
        if cur==nex:
            cnt+=1
            if cnt>=m:
                ans+=1
                break
        else:
            cnt=1
            if cnt>=m:
                ans+=1
                break
        

for j in range(n):
    cnt=1
    for i in range(n-1):
        cur,nex=arr[i][j],arr[i+1][j]
        if cur==nex:
            cnt+=1
            if cnt>=m:
                ans+=1
                break
        else:
            cnt=1
            if cnt>=m:
                ans+=1
                break
print(ans)