list = []
x = int(input("How many numbers you want to insert ?: "))
print("Enter", x, "Numbers:")
for i in range(x):
    y = int(input())
    list.append(y)

print("This is the list entered by you", list)
print("The Total sum of list is: ", sum(list))