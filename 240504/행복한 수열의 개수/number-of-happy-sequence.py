n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

cnt=0
for i in range(n):
    for j in range(n):
        if i>n:
            break
        cur=arr[i][j]
        for k in range(j,j+m):
            if j+m>n:
                continue
            if cur!=arr[i][k]:
                break
            if k==j+m-1:
                i+=1
                cnt+=1

                
        
for j in range(n):
    for i in range(n):
        if j>n:
            break
        cur=arr[i][j]
        for l in range(i,i+m):
            if i+m>n:
                continue
            if cur!=arr[l][j]:
                break
            if l==i+m-1:
                cnt+=1
                j+=1

print(cnt)