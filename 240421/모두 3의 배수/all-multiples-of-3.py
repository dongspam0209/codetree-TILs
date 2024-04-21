cnt=0
ans=0
for _ in range(5):
    a=int(input())
    if a%3==0:
        cnt+=1
    else:
        break
if cnt==5:
    ans=1
print(ans)