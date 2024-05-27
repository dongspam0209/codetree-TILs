N,B=map(int,input().split())
ans_list=[]
while True:
    if N<B:
        ans_list.append(N)
        break
    ans_list.append(N%B)
    N//=B

for num in ans_list[::-1]:
    print(num,end="")