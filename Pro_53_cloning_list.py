list = []
x = int(input("Enter No of elements: "))
print("Enter", x, "Numbers:")
for i in range(x):
    y = int(input())
    list.append(y)
print(list)
list_2 = list[:]
print(list_2)