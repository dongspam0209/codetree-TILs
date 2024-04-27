n,m=map(int,input().split())
A=list(map(int,input().split()))
index=list()
for _ in range(m):
    a_1,a_2=map(int,input().split())
    index.append((a_1,a_2))

def print_sum(arr):
    # arr : index array
    for a_1,a_2 in arr:
        print(sum(A[a_1-1:a_2]))

print_sum(index)