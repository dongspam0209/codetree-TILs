R,C=map(int,input().split())
arr=[]
cnt=0
for _ in range(R):
    arr.append(list(input().split()))
path=[[]]
cur_node=arr[0][0]
for i in range(R):
    for j in range(C):
        temp_path=[(0,0)]
        for k in range(i+1,R):
            for l in range(j+1,C):
                if arr[k][l]!=cur_node:
                    temp_path.append((k,l))
                    j=l
                    cur_node=arr[k][l]
                    break
        if temp_path[-1]==(R-1,C-1):
            path.append(temp_path)

for idx in range(len(path)):
    if len(path[idx])==4:
        cnt+=1
print(cnt)