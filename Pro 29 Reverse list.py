list = []
a = int(input("Enter no of Elements:"))
print("Enter", a, "Elements:")
for i in range(a):
    data = int(input())
    list.append(data)
print(list)
list2 = []
index = len(list)-1
# while index> -1:
#     list2.append(list[index])
#     index = index-2
for index in range(len(list)-1, -1, -1): # [4,3,2,1,0]
    list2.append(list[index])
print(list2)