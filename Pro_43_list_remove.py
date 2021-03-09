list = []
x = int(input("Enter No of elements: "))
print("Enter", x, "Numbers:")
for i in range(x):
    y = int(input())
    list.append(y)
print(list)
z = int(input("Enter the element which you want to delete: "))
list.remove(z)
print(list)