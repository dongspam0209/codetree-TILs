A=input()
cnt=0
for i in range(len(A)-2):
    for j in range(2,len(A)-1):
        if A[i]=='(' and A[i+1]=='(' and A[j]==')'and A[j+1]==')':
            cnt+=1

print(cnt)