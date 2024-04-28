n=int(input())
word_list=[]
for _ in range(n):
    word_list.append(input())

word_list.sort()
for word in word_list:
    print(word)