m_1,d_1,m_2,d_2=map(int,input().split())
A=input()
arr=[0,31,29,31,30,31,30,31,31,30,31,30,31]
first_date=sum(arr[:m_1])+d_1
second_date=sum(arr[:m_2])+d_2

diff=second_date-first_date

day_count_list=[0]*7
share=diff//7
remain=diff%7

for _ in range(share):
    for idx in range(len(day_count_list)):
        day_count_list[idx]+=1

for idx in range(remain+1):
    day_count_list[idx]+=1

day_list=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
ans_idx=0
for idx in range(len(day_list)):
    if day_list[idx]==A:
        ans_idx=idx
        
print(day_count_list[ans_idx])