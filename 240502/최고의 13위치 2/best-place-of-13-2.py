import sys
MAX_INT=-sys.maxsize
N=int(input())
arr=[]
for _  in range(N):
    arr.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N-2):
        for k in range(N):
            for l in range(N-2):
                if (k,l)==(i,j) or (k,l)==(i,j+1) or (k,l)==(i,j+2) or (k,l+2)==(i,j) or (k,l+2)==(i,j+1):
                    continue
                sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[k][l]+arr[k][l+1]+arr[k][l+2]
                MAX_INT=max(MAX_INT,sum)

print(MAX_INT)