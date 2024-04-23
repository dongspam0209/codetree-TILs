Y,M,D=map(int,input().split())
def func(Y,M,D):
    lunar_year=True # 29일 까지 있음
    if Y%4==0:
        if Y%100==0:
            lunar_year=False
        elif Y%100==0 and Y%400==0:
            lunar_year=True
        else:
            lunar_year=True
    else:
        lunar_year=False
    
    if 3<=M and M<=5:
        #spring
        if M==4:
            if D<=30:
                print("Spring")
            else:
                print("-1")
        else:
            print("Spring")
    elif 6<=M and M<=8:
        #summer
        if M==6:
            if D<=30:
                print("Summer")
            else:
                print("-1")
        else:
            print("Summer")
    elif 9<=M and M<=11:
        #fall
        if M==9 or M==11:
            if D<=30:
                print("Fall")
            else:
                print("-1")
        else:
            print("Fall")
    else:
        #winter
        if M==2:
            if lunar_year:
                if D<=29:
                    print("Winter")
                else:
                    print("-1")
            else:
                if D<=28:
                  print("Winter")
                else:
                    print("-1")
        else:
            print("Winter")

func(Y,M,D)