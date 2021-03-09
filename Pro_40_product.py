end = int(input("How many items you want to store ?  "))
list=[]
for i in range(end):

    list.append(input("Enter product's name : "))
    list.append(input("Enter product's brand: "))
    list.append(int(input("Enter product's price: ")))
    list.append(int(input("Enter product's quantity: ")))
print(list)