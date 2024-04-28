class Secret:
    def __init__(self,code,place,time):
        self.code=code
        self.place=place
        self.time=time

code,place,time=input().split()

test=Secret(code,place,time)

print("secret code :",test.code)
print("meeting point :",test.place)
print("time :",test.time)