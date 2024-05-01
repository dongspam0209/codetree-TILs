N=int(input())
space=[]
for _ in range(N):
    space.append(int(input()))

distance_list=[]
for room in range(N):
    distance=0
    for idx in range(N):
        distance_factor=0
        if idx<room:
            distance_factor=N-room+idx
        else:
            distance_factor=idx-room
        # print(distance_factor,end=" ")
        distance+=distance_factor*space[idx]
    distance_list.append(distance)

print(min(distance_list))