class Number:
    def __init__(self,number,idx=0):
        self.number=number
        self.idx=idx

N=int(input())
arr=list(map(int,input().split()))
num_list=[Number(number,idx=0)for number in arr]
sorted_num_list=sorted(num_list,key=lambda x:x.number)

for idx,num in enumerate(sorted_num_list):
    num.idx=idx+1

for num in num_list:
    print(num.idx,end=" ")