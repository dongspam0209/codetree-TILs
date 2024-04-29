n=int(input())
class People:
    def __init__(self,name,street,region):
        self.name=name
        self.street=street
        self.region=region
people_list=[]
for _ in range(n):
    name,street,region=input().split()
    people_list.append(People(name,street,region))

name_list=[]
for person in people_list:
    name_list.append(person.name)
    name_list.sort(reverse=True)

for person in people_list:
    if person.name==name_list[0]:
        print('name',person.name)
        print('addr',person.street)
        print('city',person.region)