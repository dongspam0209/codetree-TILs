m_1,d_1,m_2,d_2=map(int,input().split())
arr=[0,31,28,31,30,31,30,31,31,30,31,30,31]
A=sum(arr[:m_1])+d_1
B=sum(arr[:m_2])+d_2
difference=B-A
if difference<0:
    count=abs(difference)%7
    weekday_list=['Mon','Sun','Sat','Fri','Thu','Wed','Fri']
    print(weekday_list[count])
else:
    count=abs(difference)%7
    weekday_list=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    print(weekday_list[count])