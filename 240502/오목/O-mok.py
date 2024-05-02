# 1 black 2 white
arr=[]
for _ in range(19):
    arr.append(list(map(int,input().split())))

dx_dy=[[1,0],[1,1],[0,1],[-1,1]]
ans=[]
winner=0
for i in range(19):
    for j in range(19):
        if arr[i][j]!=0:
            cur_stone=arr[i][j]
        stone_pos=[(i,j)]
        cur_stone=arr[i][j]
        for dx,dy in dx_dy:
            next_x,next_y=i+dx,j+dy
            cnt=1
            while 0<=next_x and next_x<19 and 0<=next_y and next_y<19 and arr[next_x][next_y]==cur_stone:
                cnt+=1
                stone_pos.append((next_x,next_y))
                if cnt==5:
                    if cur_stone==1:
                        winner=1
                        ans=stone_pos
                    elif cur_stone==2:
                        winner=2
                        ans=stone_pos
                next_x+=dx  
                next_y+=dy

print(winner)
if len(ans)>=5:
    ans_x,ans_y=ans[2]
    print(ans_x+1,ans_y+1)