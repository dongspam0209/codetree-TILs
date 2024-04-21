b,a=map(int,input().split())
for idx in range(b,a-1,-1):
    if idx%2==1:
        print(idx,end=" ")