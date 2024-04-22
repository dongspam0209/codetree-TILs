N= int(input())
arr=list(map(int,input().split()))
def Max(idx,arr):
    if idx==0:
        return arr[idx]
    
    return max(Max(idx-1,arr),arr[idx])

print(Max(N-1,arr))