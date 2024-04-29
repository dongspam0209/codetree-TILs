class Student:
    def __init__(self,number,height,weight):
        self.number=number
        self.height=height
        self.weight=weight

N=int(input())
arr=[map(int,input().split())for _ in range(N)]
student_list=[Student(number+1,height,weight) for number,(height,weight) in enumerate(arr)]

# print(student_list[0].number,student_list[0].height,student_list[0].weight)
student_list.sort(key=lambda x: (-x.height,-x.weight,x.number))

for student in student_list:
    print(student.height,student.weight,student.number)