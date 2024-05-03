arr=[[0]*2000 for _ in range(2000)]
for _ in range(2):
    x_1,y_1,x_2,y_2=map(int,input().split())
    x_1,y_1,x_2,y_2=x_1+1000,y_1+1000,x_2+1000,y_2+1000
    for i in range(x_1,x_2):
        for j in range(y_1,y_2):
            arr[i][j]=1
x_1,y_1,x_2,y_2=map(int,input().split())
x_1,y_1,x_2,y_2=x_1+1000,y_1+1000,x_2+1000,y_2+1000
for i in range(x_1,x_2):
    for j in range(y_1,y_2):
        arr[i][j]=2

cnt=0
for i in range(2000):
    for j in range(2000):
        if arr[i][j]==1:
            cnt+=1

print(cnt)