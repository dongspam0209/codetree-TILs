N,M=map(int,input().split())
str_arr=[]
for _ in range(N):
    str_arr.append(input())

# 어차피 string이 list라고 상관없음

dx_dy=[(1,1),(1,-1),(1,0),(-1,1),(-1,-1),(-1,0),(0,1),(0,-1)]
ans=0
for i in range(N):
    for j in range(M):
        if str_arr[i][j]!='L':
            continue
        for dx,dy in dx_dy:
            cnt=1
            nx=i+dx
            ny=j+dy
            temp=[(i,j)]
            while True:
                if (0<=nx and nx<N and 0<=ny and ny<M)==False :
                    break
                if str_arr[nx][ny]!='E':
                    break 
                cnt+=1
                temp.append((nx,ny))
                if cnt==3:
                    ans+=1
                    # print(temp)
                    break
                nx+=dx
                ny+=dy


print(ans)