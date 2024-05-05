n=int(input())
def add(temp,k,v):    
    temp[k]=v
    return temp

def remove(temp,k):
    temp.pop(k)

def find(temp,k):
    if k in temp:
        return temp[k]
    return None

temp={}
for _ in range(n):
    string=input()
    if len(string.split())==2:
        command,k=string.split()
        if command=='remove':
            remove(temp,k)
        else:
            print(find(temp,k))
    else:
        _,k,v=string.split()
        temp=add(temp,k,v)