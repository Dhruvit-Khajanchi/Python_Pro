no1=int(input("Enter No: "))
no2=int(input("Enter No: "))
no3=int(input("Enter No: "))

if no1 > no2 and no1 > no3:
    print("No 1 is Maximum", no1)
elif no2 > no1 and no2 > no3:
    print("No 2 is Maximum", no2)
else:
    print("No 3 is Maximum", no3)