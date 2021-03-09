list = []
s = int(input("Enter number of elements: "))
print("Enter", s, "Numbers: ")
for i in range(s):
 y = int(input())
 list.append(y)

for num in list:
    if num % 2 == 0:
        print(num, end=" ")