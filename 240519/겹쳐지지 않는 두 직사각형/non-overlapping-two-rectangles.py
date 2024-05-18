import sys
MAX_INT=-sys.maxsize

n,m=map(int,input().split())
grid=[]
visit=[[0]*m for _ in range(n)]

for _ in range(n):
    grid.append(list(map(int,input().split())))

def checker_init():
    for i in range(n):
        for j in range(m):
            visit[i][j]=0

def draw(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            visit[i][j]+=1

def checker():
    for i in range(n):
        for j in range(m):
            if visit[i][j]>=2:
                return True
    return False


def check_overlapped(x1,y1,x2,y2,i,j,k,l):
    checker_init()
    draw(x1,y1,x2,y2)
    draw(i,j,k,l)
    return checker()

def rect_sum(x1,y1,x2,y2):
    return sum([grid[i][j] for i in range(x1,x2+1) for j in range(y1,y2+1)])

def rect_score_ans(x1,y1,x2,y2):
    rect_score=MAX_INT
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    if not check_overlapped(x1,y1,x2,y2,i,j,k,l):
                        rect_score=max(rect_score,rect_sum(x1,y1,x2,y2)+rect_sum(i,j,k,l))
                    

    return rect_score

MAX_INT=-sys.maxsize


for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for l in range(j,m):
                MAX_INT=max(MAX_INT,rect_score_ans(i,j,k,l))

print(MAX_INT)