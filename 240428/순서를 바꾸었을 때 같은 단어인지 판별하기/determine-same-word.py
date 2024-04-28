A=input()
B=input()
A=list(A)
B=list(B)
A.sort()
B.sort()

check=True
for idx in range(len(A)):
    if A[idx]!=B[idx]:
        check=False
        
if check:
    print("Yes")
else:
    print("No")