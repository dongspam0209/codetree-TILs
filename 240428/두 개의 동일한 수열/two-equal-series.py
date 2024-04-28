n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
check_A=sorted(A)
check_B=sorted(B)

check=True
for idx in range(len(check_A)):
    if check_A[idx]!=check_B[idx]:
        check=False

if check:
    print("Yes")
else:
    print("No")