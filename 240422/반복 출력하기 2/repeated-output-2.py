def hello(n):
    if n==0:
        return
    hello(n-1)
    print("HelloWorld")

n=int(input())
hello(n)