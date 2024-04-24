a,b=map(int,input().split())
def three_six_nine(n):
    n=str(n)
    flag=False
    if '3' in n or '6' in n or '9' in n:
        flag=True
    return flag

def three_multiply(n):
    return n%3==0

cnt=0
for num in range(a,b+1):
    if three_multiply(num) or three_six_nine(num):
        cnt+=1

print(cnt)