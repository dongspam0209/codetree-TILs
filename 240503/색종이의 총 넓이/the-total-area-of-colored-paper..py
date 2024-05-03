N=int(input())
arr=[[0]*1000 for _ in range(1000)]
for _ in range(N):
    x,y=map(int,input().split())
    x+=100
    y+=100
    for i in range(x,x+8):
        for j in range(y,y+8):
            arr[i][j]=1
cnt=0
for i in range(1000):
    for j in range(1000):
        if arr[i][j]==1:
            cnt+=1

print(cnt)