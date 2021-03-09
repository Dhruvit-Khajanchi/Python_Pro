list = []
x = int(input("Enter No of elements: "))
print("Enter", x, "Numbers:")
for i in range(x):
    y = int(input())
    list.append(y)
print(list)
list[0], list[-1] = list[-1], list[0]
print(list)