class Student:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

n=int(input())
arr=[(input().split()) for _ in range(n)]
student_list=[Student(name,int(height),int(weight))for name,height,weight in arr]
student_list.sort(key=lambda x : (x.height,-x.weight))
for student in student_list:
    print(student.name,student.height,student.weight)