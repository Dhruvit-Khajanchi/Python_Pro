list=[]
x=int(input("Enter No of elements: "))
print("Enter", x, "Numbers:")
for i in range(x):
    y=int(input())
    list.append(y)
print(list)
z=0
while z<len(list):
    print(list[z])
    z+=2