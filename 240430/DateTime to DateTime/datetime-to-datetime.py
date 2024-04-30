a,b,c=map(int,input().split())#일 시 분
A=10*24*60+11*60+11
B=(a-1)*24*60+b*60+c
if B-A>=0:
    print(B-A)
else:
    print(-1)