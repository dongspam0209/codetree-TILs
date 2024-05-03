s=input()
s=list(s)
# s[0]='a'
s[1]='a'
s[len(s)-2]='a'
# s[len(s)-1]='a'

t=''.join(s)
print(t)