import sys
MAX_INT=-sys.maxsize
N=int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))

for i in range(N-2):
    for j in range(N-2):
        sum=0
        for k in range(i,i+3):
            for l in range(j,j+3):
                sum+=arr[k][l]
        MAX_INT=max(MAX_INT,sum)
        
print(MAX_INT)