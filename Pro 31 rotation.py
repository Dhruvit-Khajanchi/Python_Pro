list = []
x = int(input("Enter Range of list: "))
print("Enter", x, "Elements")
for i in range(x):
    y = int(input("Enter No.: "))
    list.append(y)
print("Your list is: ", list)
for y in range(1, x):
    list[y], list[0] = list[0], list[y]
# list[1], list[0] = list[0], list[1]
# list[2], list[0] = list[0], list[2]
# list[3], list[0] = list[0], list[3]
# list[4], list[0] = list[0], list[4]
print("List after rotation", list)