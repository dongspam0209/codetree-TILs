N=int(input())
arr=[]
for idx in range(N):
    arr.append(int(input()))
for num in arr:
    if num%3==0 and num%2==1:
        print(num)