n=list(map(int,input()))
decimal=0
exp=0
for bit in n[::-1]:
    decimal+=2**exp*bit
    exp+=1
print(decimal)