n,m=map(int,input().split())
string_dict={}
index_dict={}
tmp_arr=[]
for _ in range(n):
    tmp_arr.append(input())

for idx,elem in enumerate(tmp_arr):
    string_dict[elem]=idx+1
    index_dict[idx+1]=elem

for _ in range(m):
    s=input()
    if s in string_dict:
        print(string_dict[s])
    else:
        s=int(s)
        print(index_dict[s])