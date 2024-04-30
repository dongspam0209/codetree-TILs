N=int(input())
class Student:
    def __init__(self,number,height,weight):
        self.number=number
        self.height=height
        self.weight=weight

arr=[(map(int,input().split()))for _ in range(N)]
student_list=[Student(idx+1,height,weight)for idx,(height,weight) in enumerate(arr)]
student_list.sort(key=lambda x: (x.height,-x.weight))

for student in student_list:
    print(student.height,student.weight,student.number)