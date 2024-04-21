n=int(input())
for i in range(n):
    num_stars=2*i+1
    for _ in range(num_stars):
        print("*",end="")
    print()