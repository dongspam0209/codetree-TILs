a=int(input())
for num in range(1,a+1):
    check=num//8
    if not (num%2==0 and num%4!=0) and not check%2==0 and not num%7<4:
        print(num,end=" ")