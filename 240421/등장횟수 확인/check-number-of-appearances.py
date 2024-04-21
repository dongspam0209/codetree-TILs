arr=[]
for _ in range(5):
    arr.append(int(input()))
ans=0
for num in arr:
    if num%2==0:
        ans+=1

print(ans)