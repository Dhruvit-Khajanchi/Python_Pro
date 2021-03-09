start = 0
sum = 200
x = int(input("Enter No. of Calls: "))
if x <= 100:
    print("Your Bill is 200 Rs/-")
elif x <= 150:
    sum = (x-100)*0.60+200
    print("Your Bill is", sum, "Rs/-")
elif x <= 200:
    sum = 50 * 0.60 + 200+(x-150)*0.50
    print("Your Bill is", sum, "Rs/-")
elif x > 200:
    sum = 50 * 0.60 + 200+50 * 0.50+(x-200)*0.40
    print("Your Bill is", sum, "Rs/-")