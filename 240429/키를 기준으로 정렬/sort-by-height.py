class Student:
    def __init__(self,name,height,width):
        self.name=name
        self.height=height
        self.width=width
n=int(input())
arr=[input().split() for _ in range(n)]
student_list=[Student(name,int(height),width) for name,height,width in arr]
student_list.sort(key=lambda x:x.height)

for idx in student_list:
    print(idx.name,idx.height,idx.width)