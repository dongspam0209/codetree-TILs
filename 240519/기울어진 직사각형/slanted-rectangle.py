import sys
MAX_INT=-sys.maxsize
n=int(input())
grid=[]
for _ in range(n):
    grid.append(list(map(int,input().split())))

def is_range(i,j):
    return 0<=i and i<n and 0<=j and j<n

def score(x,y,k,l): # k는 직사각형의 가로 l은 직사각형의 세로
    dx_dy=[(-1,1),(-1,-1),(1,-1),(1,1)]
    move_cnt=[k,l,k,l]
    rect_score=0
    for (dx,dy),move_cnt in zip(dx_dy,move_cnt):
        for itr in range(move_cnt):
            x+=dx
            y+=dy

            if is_range(x,y)==False:
                return 0
            
            rect_score+=grid[x][y]
    return rect_score

for i in range(n):
    for j in range(n):
        for k in range(1,n):
            for l in range(1,n):
                MAX_INT=max(MAX_INT,score(i,j,k,l))


print(MAX_INT)