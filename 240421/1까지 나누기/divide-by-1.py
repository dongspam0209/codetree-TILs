n=int(input())
cnt=0
idx=1
while n>1:
    n//=idx
    print(n)
    cnt+=1
    idx+=1
print(cnt)