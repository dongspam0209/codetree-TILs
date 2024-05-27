n=int(input())
digit=[]
while True:
    if n<2:
        digit.append(n)
        break
    digit.append(n%2)
    n//=2

for idx in digit[::-1]:
    print(idx,end="")