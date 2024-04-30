a,b,c=map(int,input().split())
day=(a-11)*60*24
hour=(b-11)*60
minute=c-11

if day<0:
    print(-1)
else:
    if hour<0:
        print(-1)
    else:
        if minute<0:
            print(-1)
        else:
            print(day+hour+minute)