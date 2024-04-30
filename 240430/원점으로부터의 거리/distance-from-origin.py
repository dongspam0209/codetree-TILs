class Point:
    def __init__(self,idx,x,y):
        self.idx=idx
        self.x=x
        self.y=y

N=int(input())
arr=[(map(int,input().split()))for _ in range(N)]
Points=[Point(idx+1,x,y)for idx,(x,y) in enumerate(arr)]
Points.sort(key=lambda point: abs(point.x-0) + abs(point.y-0))
for point in Points:
    print(point.idx)