age_sum=0
cnt=0
while True:
    age=int(input())
    if age>=20 and age<30:
        age_sum+=age
        cnt+=1
    else:
        break
print(f"{age_sum/cnt:.2f}")