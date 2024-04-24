n=int(input())
def check(n):
    return (n//10+n%10)%5==0

toggle=check(n)
if toggle:
    print("Yes")
else:
    print("No")