a,b=map(int,input().split())
n=list(map(int,input()))

pow_idx=0
dec=0
for idx in n:
    dec+=idx*a**pow_idx
    pow_idx+=1

ans_list=[]
while True:
    if dec<b:
        ans_list.append(dec)
        break
    ans_list.append(dec%b)
    dec//=b

for i in ans_list[::-1]:
    print(i,end="")