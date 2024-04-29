code,color,sec=input().split()
sec=int(sec)
class Bomb:
    def __init__(self,code,color,sec):
        self.code=code
        self.color=color
        self.sec=sec
test=Bomb(code,color,sec)
print('code :',test.code)
print('color :',test.color)
print('second :',test.sec)