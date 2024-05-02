# # 1 black 2 white
# arr=[]
# for _ in range(19):
#     arr.append(list(map(int,input().split())))

# dx_dy=[[1,0],[1,1],[0,1],[-1,1]]
# ans=[]
# winner=0
# for i in range(19):
#     for j in range(19):
#         if arr[i][j]!=0:
#             cur_stone=arr[i][j]
#         stone_pos=[(i,j)]
#         cur_stone=arr[i][j]
#         for dx,dy in dx_dy:
#             next_x,next_y=i+dx,j+dy
#             cnt=1
#             while 0<=next_x and next_x<19 and 0<=next_y and next_y<19 and arr[next_x][next_y]==cur_stone:
#                 cnt+=1
#                 stone_pos.append((next_x,next_y))
#                 if cnt==5:
#                     if cur_stone==1:
#                         winner=1
#                         ans=stone_pos
#                     elif cur_stone==2:
#                         winner=2
#                         ans=stone_pos
#                 next_x+=dx  
#                 next_y+=dy

# print(winner)
# if len(ans)>=5:
#     ans_x,ans_y=ans[2]
#     print(ans_x+1,ans_y+1)
import sys

# 변수 선언 및 입력
arr = [
    list(map(int, input().split()))
    for _ in range(19)
]

def in_range(x, y):
    return 0 <= x and x < 19 and 0 <= y and y < 19

dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]

# 모든 좌표에서 다 확인해봅니다.
for i in range(19):
	# 격자를 벗어나지 않을 범위로만 잡습니다.
	for j in range(19):
		
		if arr[i][j] == 0:
			continue
		
		for dx, dy in zip(dxs, dys):
			curt = 1
			curx = i
			cury = j
			while True:
				nx = curx + dx
				ny = cury + dy
				if in_range(nx, ny) == False:
					break
				if arr[nx][ny] != arr[i][j]:
					break
				curt += 1
				curx = nx
				cury = ny
			
			if curt == 5:
				print(arr[i][j])
				print(i + 2 * dx + 1, j + 2 * dy + 1)
				sys.exit()

print(0)