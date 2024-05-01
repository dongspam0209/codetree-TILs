# import sys
# MIN_INT=sys.maxsize

# N=int(input())
# checkpoints=[]
# for _ in range(N):
#     checkpoints.append(list(map(int,input().split())))

# for except_point in range(1,len(checkpoints)):
#     temp_checkpoints=[]
#     for j in range(len(checkpoints)):
#         if j!=except_point:
#             temp_checkpoints.append(checkpoints[j])
#     distance=0
#     for i in range(1,len(checkpoints)-1):
#         x_1,y_1=temp_checkpoints[i-1][0],temp_checkpoints[i-1][1]
#         x_2,y_2=temp_checkpoints[i][0],temp_checkpoints[i][1]
#         distance+=abs(x_2-x_1)+abs(y_2-y_1)
#     MIN_INT=min(distance,MIN_INT)
# print(MIN_INT)
import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n = int(input())
arr = [
	list(map(int, input().split()))
	for _ in range(n)
]

# 각 i번째 체크포인트를 건너 뛰었을 때의 거리를 구해줍니다.
ans = INT_MAX
for i in range(1, n - 1):
	# 거리를 구합니다.
	dist = 0
	prev_idx = 0
	for j in range(1, n):
		if j == i:
			continue
		dist += abs(arr[prev_idx][0] - arr[j][0]) + abs(arr[prev_idx][1] - arr[j][1])
		prev_idx = j
	
	ans = min(ans, dist)

# 출력
print(ans)