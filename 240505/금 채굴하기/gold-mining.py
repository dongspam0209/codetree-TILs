import sys
MAX_INT=-sys.maxsize
n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        for k in range(1,5):
            cost=0
            for x in range(-k,k+1):
                if j+x < 0 or j+x>=n:
                    continue
                for y in range(1,k-abs(x)+1):
                    if i-y<0:
                        continue
                    cost+=arr[i-y][j+x]
                
                for y in range(1,k-abs(x)+1):
                    if i+y>=n:
                        continue
                    cost+=arr[i+y][j+x]

                cost+=arr[i][j+x]
            if m*cost-k**2-(k+1)**2>=0:
                # print('k:',k,'i,j:',(i,j),cost)
                MAX_INT=max(MAX_INT,cost)

for i in range(n):
    for j in range(n):
        cost=0
        cost+=arr[i][j]
        if m*cost>=1:
            MAX_INT=max(MAX_INT,cost)


print(MAX_INT)