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

print('name',people_list[-1].name)
print('addr',people_list[-1].street)
print('city',people_list[-1].region)