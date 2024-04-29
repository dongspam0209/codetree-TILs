class Student:
    def __init__(self,name,kor,eng,math):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math

n=int(input())
arr=[input().split() for _ in range(n)]
student_list=[Student(name,int(kor),int(eng),int(math)) for name,kor,eng,math in arr]
student_list.sort(key=lambda x : (-x.kor,-x.eng,-x.math))

for student in student_list:
    print(student.name,student.kor,student.eng,student.math)