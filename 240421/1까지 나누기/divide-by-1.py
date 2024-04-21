n=int(input())
cnt=0
idx=0
while n>1:
    idx+=1
    n/=idx
    if n>1:
        cnt+=1

print(cnt)