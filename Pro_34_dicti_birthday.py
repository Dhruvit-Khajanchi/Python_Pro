dic = {'Alice': 'May 16', 'David': 'Aug 31', 'Allen': 'March 18'}
while True:
    name = input("Enter Name: ")
    if name == ():
        break
    if name in dic :
        print(dic[name], "is the birthday of", name)
    else:
        print("I do not have birthday information of", name)
        print("When is their birthday ?")
        birthday = input(" ")
        dic.__setitem__(name, birthday)
        print("Database has been Updated!!")