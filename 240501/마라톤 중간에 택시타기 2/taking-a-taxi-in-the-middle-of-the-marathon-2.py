import sys
MIN_INT=sys.maxsize

N=int(input())
checkpoints=[]
for _ in range(N):
    checkpoints.append(list(map(int,input().split())))

for except_point in range(1,len(checkpoints)):
    temp_checkpoints=[]
    for j in range(len(checkpoints)):
        if j!=except_point:
            temp_checkpoints.append(checkpoints[j])
    distance=0
    for i in range(1,len(checkpoints)-1):
        x_1,y_1=temp_checkpoints[i-1][0],temp_checkpoints[i-1][1]
        x_2,y_2=temp_checkpoints[i][0],temp_checkpoints[i][1]
        distance+=abs(x_2-x_1)+abs(y_2-y_1)
    MIN_INT=min(distance,MIN_INT)
print(MIN_INT)