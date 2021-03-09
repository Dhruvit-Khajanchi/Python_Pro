list=[]
s=int(input("Enter no of elements: "))
print("Enter", s,"Elements:")
for i in range(s):
    p=int(input())
    list.append(p)
print(list)
list.sort(reverse=True)
print(list)