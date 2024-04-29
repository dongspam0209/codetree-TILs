class Product:
    def __init__(self,name='codetree',code=50):
        self.name=name
        self.code=code
test_1=Product()
name,code=input().split()
test_2=Product(name,code)
print('product',test_1.code,'is',test_1.name)
print('product',test_2.code,'is',test_2.name)