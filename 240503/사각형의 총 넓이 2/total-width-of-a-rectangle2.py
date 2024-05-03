N=int(input())
arr=[[0]*200 for _ in range(200)]
# print(arr)
for _ in range(N):
    x_1,y_1,x_2,y_2=map(int,input().split())
    x_1,y_1,x_2,y_2=x_1+100,y_1+100,x_2+100,y_2+100
    for i in range(x_1,x_2):
        for j in range(y_1,y_2):
            arr[i][j]=1

cnt=0
for i in range(200):
    for j in range(200):
        if arr[i][j]==1:
            cnt+=1

print(cnt)