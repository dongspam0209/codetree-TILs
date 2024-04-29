class Test:
    def __init__(self,Id='codetree',level=10):
        self.Id=Id
        self.level=level
temp=Test()
a,b=input().split()
temp2=Test(a,b)
print('user',temp.Id,'lv',temp.level)
print('user',temp2.Id,'lv',temp2.level)