y=int(input())
def func(y):
    check=True
    if y%4==0:
        return check
    if y%100==0 and y%400!=0:
        return check
    else:
        check=False
        return check

if func(y):
    print("true")
else:
    print("false")