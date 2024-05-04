import sys
MAX_INT=-sys.maxsize

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

#case 1

for i in range(n):
    case_1=0
    case_2=0
    case_3=0
    case_4=0

    for j in range(m):
        if i+2>n or j+2>m:
            continue
        case_1=arr[i][j]+arr[i+1][j]+arr[i+1][j+1]
        case_2=arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]
        case_3=arr[i][j]+arr[i+1][j]+arr[i][j+1]
        case_4=arr[i][j]+arr[i+1][j+1]+arr[i][j+1]
        MAX_INT=max(case_1,case_2,case_3,case_4,MAX_INT)
        
for i in range(n):
    for j in range(m):
        case_1=0
        case_2=0
        for k in range(i,i+3):
            if i+3>n:
                continue
            case_1+=arr[k][j]
        MAX_INT=max(case_1,MAX_INT)
        for l in range(j,j+3):
            if j+3>m:
                continue
            case_2+=arr[i][l]
        MAX_INT=max(case_1,case_2,MAX_INT)

print(MAX_INT)