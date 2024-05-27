N=list(map(int,input()))
pow_idx=0
decimal=0
for bin_num in N[::-1]:
    decimal+=bin_num*2**pow_idx
    pow_idx+=1
new_decimal=decimal*17

new_binary=[]
while True:
    if new_decimal<2:
        new_binary.append(new_decimal)
        break
    new_binary.append(new_decimal%2)
    new_decimal//=2

for bin_num in new_binary[::-1]:
    print(bin_num,end="")