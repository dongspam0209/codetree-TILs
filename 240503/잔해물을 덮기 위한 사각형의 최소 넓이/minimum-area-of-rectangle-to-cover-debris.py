import sys

arr=[[0]*2000 for _ in range(2000)]
for case in range(2):
    x_1,y_1,x_2,y_2=map(int,input().split())
    x_1+=1000
    x_2+=1000
    y_1+=1000
    y_2+=1000
    if case == 1:
        for i in range(x_1,x_2+1):
            for j in range(y_1,y_2+1):
                arr[i][j]=2
    else:
        for i in range(x_1,x_2+1):
            for j in range(y_1,y_2+1):
                arr[i][j]=1

rect_1_pos=[]
for i in range(2000):
    for j in range(2000):
        if arr[i][j]==1:
            rect_1_pos.append((i,j))
# print(rect_1_pos)
MAX_X=-sys.maxsize
MAX_Y=-sys.maxsize
MIN_X=sys.maxsize
MIN_Y=sys.maxsize

for x,y in rect_1_pos:
    MAX_X=max(x,MAX_X)
    MAX_Y=max(y,MAX_Y)
    MIN_X=min(x,MIN_X)
    MIN_Y=min(y,MIN_Y)

# print(MAX_X,MAX_Y,MIN_X,MIN_Y)
print((MAX_X-MIN_X)*(MAX_Y-MIN_Y))