# n=int(input())
# class People:
#     def __init__(self,name,street,region):
#         self.name=name
#         self.street=street
#         self.region=region
# people_list=[]
# for _ in range(n):
#     name,street,region=input().split()
#     people_list.append(People(name,street,region))

# name_list=[]
# for person in people_list:
#     name_list.append(person.name)
#     name_list.sort(reverse=True)

# for person in people_list:
#     if person.name==name_list[0]:
#         print('name',person.name)
#         print('addr',person.street)
#         print('city',person.region)
class Address:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region
        
        
# 변수 선언 및 입력
n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people = [Address(name, address, region) for name, address, region in arr]

# 사전순으로 이름이 가장 느린 사람 찾기
target_idx = 0
for i, person in enumerate(people):
    if person.name > people[target_idx].name:
        target_idx = i

# 결과 출력
print(f"name {people[target_idx].name}")
print(f"addr {people[target_idx].address}")
print(f"city {people[target_idx].region}")