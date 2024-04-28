n,k,T=input().split()
n=int(n)
k=int(k)-1
words=[]
for _ in range(n):
    word=input()
    if word.startswith(T):
        words.append(word)
    
words.sort()
print(words[k])