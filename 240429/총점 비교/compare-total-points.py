class Student:
    def __init__(self,name,a,b,c):
        self.name=name
        self.a=a
        self.b=b
        self.c=c
n=int(input())
arr=[input().split() for _ in range(n)]
student_list=[Student(name,int(a),int(b),int(c))for name,a,b,c in arr]
student_list.sort(key=lambda x: x.a+x.b+x.c)
for student in student_list:
    print(student.name,student.a,student.b,student.c)