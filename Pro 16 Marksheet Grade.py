n=input("Enter your name: ")
r=int(input("Enter your roll no.: "))
m=float(input("Enter Maths marks:  "))
e=float(input("Enter English marks: "))
s=float(input("Enter Science marks: "))

sum=m+s+e
avg=sum/3
if avg>=90 and avg<=100 :
    print("You have acquired A")
elif avg>=80 and avg<=89:
    print("You have acquired B")
elif avg>=70 and avg<=79:
    print("You have acquired C")
elif avg>=69 and avg<=60:
    print("You have acquired D")
else :
    print("You have Failed!!")