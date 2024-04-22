n=int(input())
def _sum(n):
    if n==0:
        return n
    return _sum(n-1)+n

print(_sum(n))