list = []
x = int(input("Enter No of elements: "))
print("Enter", x, "Numbers: ")
for i in range(x):
    y = int(input())
    list.append(y)
print(list)
s = int(input("Enter the element which you want to check in the list: "))
if s in list:
    print("Yes This Element exists in the list.")
else:
    print("This element does not exist in the list.")