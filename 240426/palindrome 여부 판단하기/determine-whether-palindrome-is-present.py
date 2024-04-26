A=input()
def func(A):
    for idx in range((len(A))//2+1):
        if A[idx]!=A[-(idx+1)]:
            return False
    return True

if func(A):
    print("Yes")
else:
    print("No")