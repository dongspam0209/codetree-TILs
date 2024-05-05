from collections import defaultdict

n,m=map(int,input().split())

n_arr=list(map(int,input().split()))
m_arr=list(map(int,input().split()))


n_dict=defaultdict(list) # 각 숫자별로 볓번째에 위치하는지 알려줌.

for i,elem in enumerate(n_arr):
    n_dict[elem].append(i+1)

for m in m_arr:
    print(len(n_dict[m]),end=" ")