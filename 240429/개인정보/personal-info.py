class People:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
arr=[(input().split()) for _  in range(5)]
people_list=[People(name,int(height),weight) for name,height,weight in arr]
a=sorted(people_list,key=lambda x : x.name)
print('name')
for person in a:
    print(person.name,person.height,person.weight)
b=sorted(people_list,key=lambda x : -x.height)
print()
print('height')
for person in b:
    print(person.name,person.height,person.weight)