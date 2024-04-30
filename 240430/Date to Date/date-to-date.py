m1,d1,m2,d2=map(int,input().split())
def func(month):
    return sum(day_arr[:month])
day_arr=[0,31,28,31,30,31,30,31,31,30,31,30,31]
A=func(m1)+d1
B=func(m2)+d2
print(B-A+1)