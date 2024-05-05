from collections import defaultdict
n=int(input())
tmp_dict=defaultdict(int)
for _ in range(n):
    s=input()
    tmp_dict[s]+=1

sorted_dict=sorted(tmp_dict.items(),key=lambda x: x[1])
print(sorted_dict[-1][1])