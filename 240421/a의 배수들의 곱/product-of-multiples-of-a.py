ans=1
a,b=map(int,input().split())
for num in range(1,b+1):
    if num%a==0:
        ans*=num

print(ans)