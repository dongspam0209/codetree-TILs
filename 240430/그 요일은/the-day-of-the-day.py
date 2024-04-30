m_1,d_1,m_2,d_2=map(int,input().split())
A=input()
arr=[0,31,29,31,30,31,30,31,31,30,31,30,31]
first_date=sum(arr[:m_1])+d_1
second_date=sum(arr[:m_2])+d_2

diff=second_date-first_date

share=diff//7
remain=diff%7
day_list=[share]*7
for idx in range(remain+1):
    day_list[idx]+=1

weekday_list=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

for idx in range(len(weekday_list)):
    if weekday_list[idx]==A:
        print(day_list[idx])