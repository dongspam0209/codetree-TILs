ans=0
list_temp=[]
for _ in range(2):
    temp_dict={}
    temp_dict['age'],temp_dict['gender']=input().split()
    temp_dict['age']=int(temp_dict['age'])
    # print(temp_dict)
    list_temp.append(temp_dict)
for temp_dict in list_temp:
    if temp_dict['age']>=19 and temp_dict['gender']=='M':
        ans=1
print(ans)