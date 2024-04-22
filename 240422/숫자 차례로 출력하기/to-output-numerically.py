n=int(input())
def up(n):
    if n==0:
        return
    up(n-1)
    print(n,end=" ")

def down(n):
    if n==0:
        return
    print(n,end=" ")
    down(n-1)
    

up(n)
print()
down(n)