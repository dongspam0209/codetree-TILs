R,C=map(int,input().split())
arr=[]
for _ in range(R):
    arr.append(list(input().split()))
if arr[0][0]==arr[-1][-1]:
    print(0)
    exit()

next_node=[]
next_next_node=[]
for i in range(1,R):
    for j in range(1,C):
        if arr[i][j]!=arr[0][0] and not(i==R-1 and j==C-1):
            next_node.append((i,j))
# print(next_node)
for i,j in next_node:
    for k in range(i+1,R-1):
        for l in range(j+1,C-1):
            if arr[i][j]!=arr[k][l] and not(i==R-1 and j==C-1):
                next_next_node.append((k,l))
print(len(next_next_node))